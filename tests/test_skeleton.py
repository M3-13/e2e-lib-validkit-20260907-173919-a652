import pathlib

import pytest

import validkit
from validkit._validation import _check_length

NINE_NAMES = [
    "is_valid_email",
    "luhn_check",
    "is_valid_iban",
    "is_valid_isbn13",
    "normalize_phone",
    "strip_accents",
    "mask_secret",
    "slugify",
    "clamp",
]


def test_import_works():
    assert validkit is not None


def test_all_nine_names_are_present_and_callable():
    for name in NINE_NAMES:
        assert hasattr(validkit, name), f"{name} fehlt in validkit"
        assert callable(getattr(validkit, name)), f"{name} ist nicht aufrufbar"


def test_all_nine_names_are_exported():
    assert set(NINE_NAMES).issubset(set(validkit.__all__))


def test_check_length_allows_exactly_1024_chars():
    _check_length("a" * 1024, what="text")


def test_check_length_rejects_1025_chars():
    with pytest.raises(ValueError):
        _check_length("a" * 1025, what="text")


FORBIDDEN_CALLS = ["eval", "exec", "compile", "pickle.loads", "subprocess"]


def test_no_forbidden_calls_in_source():
    package_dir = pathlib.Path(validkit.__file__).parent
    for source in package_dir.glob("*.py"):
        code = source.read_text(encoding="utf-8")
        for token in FORBIDDEN_CALLS:
            assert token not in code, f"verbotener Aufruf {token!r} in {source.name}"
