import pytest

from validkit.isbn13 import is_valid_isbn13


def test_valid_isbn13_returns_true():
    assert is_valid_isbn13("9780306406157") is True


def test_isbn13_with_hyphens_and_spaces_returns_true():
    assert is_valid_isbn13("978-0-306-40615-7") is True
    assert is_valid_isbn13("978 0 306 40615 7") is True


def test_isbn13_with_wrong_check_digit_returns_false():
    assert is_valid_isbn13("9780306406158") is False


def test_isbn13_with_wrong_length_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("97803064061")
    with pytest.raises(ValueError):
        is_valid_isbn13("97803064061570")


def test_isbn13_with_non_digit_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("978030640615X")


def test_isbn13_longer_than_1024_characters_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("9" * 1025)
