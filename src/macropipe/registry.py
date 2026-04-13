import typing as t


class Registry:
    """Macropipe function registry"""

    r: t.ClassVar[t.Dict[str, t.Callable]] = {}

    @classmethod
    def register(cls, fn: t.Callable) -> str:
        """Register a Macropipe recipe function."""
        name = getattr(fn, "__name__", str(repr(fn)))
        if name in cls.r:
            raise ValueError(f"Macropipe function already registered: {name}")
        cls.r[name] = fn
        return name

    @classmethod
    def get(cls, name: str) -> t.Callable:
        """Get a Macropipe recipe function by name."""
        if name not in cls.r:
            raise NotImplementedError(f"Macropipe function not implemented: {name}")
        return cls.r[name]


def recipe(function: t.Callable) -> t.Callable:
    """Decorator to register a Macropipe recipe function."""
    Registry.register(function)
    return function
