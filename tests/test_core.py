import re

import pytest

from macropipe import MacroPipe
from macropipe.registry import Registry


def test_registry_register():
    """Validate the recipe function registry."""

    # Register a function manually.
    def fun():
        pass

    Registry.register(fun)
    assert Registry.get("fun") == fun

    # Registering a function twice should fail.
    with pytest.raises(ValueError) as excinfo:
        Registry.register(fun)
    assert excinfo.match("Macropipe function already registered: fun")


def test_core_decode_expression_success():
    """Validate the `decode_expression` core method."""
    assert MacroPipe.decode_expression("foo") == ("foo", [])
    assert MacroPipe.decode_expression("foo:bar") == ("foo", ["bar"])


def test_core_decode_expression_errors():
    """
    Validate error cases of the `decode_expression` core method.

    Avoid uncaught unpacking errors when expression is empty or delimiter-only.
    """

    # Empty expression.
    with pytest.raises(ValueError) as excinfo:
        MacroPipe.decode_expression(None)
    assert excinfo.match("Invalid Macropipe expression: None")

    with pytest.raises(ValueError) as excinfo:
        MacroPipe.decode_expression("")
    assert excinfo.match("Invalid Macropipe expression: ")

    # Delimiter-only expression.
    with pytest.raises(ValueError) as excinfo:
        MacroPipe.decode_expression(":::")
    assert excinfo.match("Invalid Macropipe expression: ':::'")

    # Dangling trailing escapes.
    with pytest.raises(ValueError) as excinfo:
        MacroPipe.decode_expression("concat:a:\\")
    assert excinfo.match(re.escape(r"Invalid Macropipe expression: 'concat:a:\\'"))
