"""
A small macro language on top of Polars.

This pipeline wrapper uses macro-like commands / a text-based expression language,
that uses Polars pipes to apply compiled UDFs to a LazyFrame in a structured way.

https://macropipe.readthedocs.io/
"""

import dataclasses
import re
import typing as t

import polars as pl

from macropipe.registry import Registry
from macropipe.util import ignoreargs


@dataclasses.dataclass
class MacroPipe:
    """A miniature transformation engine based on Polars."""

    expressions: t.List[str]
    registry: t.ClassVar[Registry] = Registry()
    _reserved_mp_helpers: t.ClassVar[t.Set[str]] = {"apply"}

    @classmethod
    def from_recipes(cls, *recipes: str) -> "MacroPipe":
        """Create MacroPipe from list of recipes (text-based macro commands)."""
        return cls(expressions=list(recipes))

    def resolve_function(self, name: str, lf: t.Optional[pl.LazyFrame] = None) -> t.Callable:
        """
        Resolve macro function by name, either from builtins or from user-registered function.
        """
        mp_namespace = getattr(lf, "mp", None) if lf is not None else None
        function = getattr(mp_namespace, name, None) if mp_namespace is not None else None
        if (
            callable(function)
            and not name.startswith("_")
            and name not in self._reserved_mp_helpers
        ):
            # When invoking the extension function in the `lf.mp` namespace,
            # the procedure needs to strip away the first argument.
            return ignoreargs(function, 1)
        # When invoking a user-registered function,
        # it can be invoked without further ado.
        return self.registry.get(name)

    @staticmethod
    def decode_expression(expression: str) -> t.Tuple[str, t.List[str]]:
        """
        Tokenize the expression and convert it to macro invocation descriptor.

        In contrast to the Python-based API, Macropipe invents a simple text-based
        macro language that compiles to Polars LazyFrame transformations:
        Function name and positional arguments are separated by colons ``:``,
        that's it. Use ``\:`` to represent a literal colon inside an argument.
        ::

            <function>:<arg1>:<arg2>:<arg3>

        .. todo::

            The expression language is currently pretty flat.
            It can certainly be improved in future iterations.
            Any suggestions are very much welcome.
        """

        if not expression:
            raise ValueError(f"Invalid Macropipe expression: {expression!r}")

        # Reject dangling trailing escapes before tokenization.
        # A malformed expression ending with an unmatched backslash silently loses
        # data during tokenization (e.g., concat:a:\ tokenizes to ['concat', 'a']
        # with the final \ dropped), which leads to confusing downstream behaviour.
        trailing_backslashes = len(expression) - len(expression.rstrip("\\"))
        if trailing_backslashes % 2:
            raise ValueError(f"Invalid Macropipe expression: {expression!r}")

        # Tokenize by colons but read escaped colons literally.
        tokens = re.findall(r"(?:[^:\\]|\\.)+", expression)
        if not tokens:
            raise ValueError(f"Invalid Macropipe expression: {expression!r}")
        function_name, *args = tokens
        args = [a.replace("\\:", ":") for a in args]

        return function_name, args

    def apply(self, lf: pl.LazyFrame) -> pl.LazyFrame:
        """Convert transformation recipes to Polars expressions and apply to structured pipeline."""

        # Convert all macro expressions to Polars LazyFrame transformations.
        for expression in self.expressions:
            # Decode macro expression into macro invocation descriptor.
            function_name, function_args = self.decode_expression(expression)

            # Resolve UDF from Macropipe built-ins or user-registered functions.
            function = self.resolve_function(function_name, lf)

            # Add transformation to pipeline.
            lf = lf.pipe(function, *function_args)

        return lf
