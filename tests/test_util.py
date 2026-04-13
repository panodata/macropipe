import pytest

from macropipe.util import decode_list, gettype, to_json


def test_util_gettype():
    """Validate the `gettype` utility function."""

    assert gettype("str") is str
    assert gettype("float") is float

    with pytest.raises(ValueError) as excinfo:
        gettype("Hotzenplotz")
    assert excinfo.match("Symbol does not exist: Hotzenplotz")

    with pytest.raises(ValueError) as excinfo:
        gettype("print")
    assert excinfo.match("Resolved symbol is not a Python type: print")


def test_util_decode_list():
    """Validate the `decode_list` utility function."""
    assert decode_list("a,b") == ["a", "b"]
    assert decode_list(["a", "b"]) == ["a", "b"]


def test_util_to_json():
    """Validate the `to_json` utility function."""
    assert to_json(None) is None
    assert to_json("{'foo': 'bar'}") == '{"foo":"bar"}'
    assert to_json("Hotzenplotz") is None
    with pytest.raises(ValueError) as excinfo:
        to_json("Hotzenplotz", strict=True)
    assert excinfo.match("malformed")
