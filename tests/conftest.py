import pytest

from macropipe.registry import Registry


@pytest.fixture(autouse=True)
def _restore_registry():
    """Isolate global Registry mutations to keep tests order-independent."""
    snapshot = Registry.r.copy()
    yield
    Registry.r = snapshot
