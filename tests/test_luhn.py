import pytest

from validkit.luhn import luhn_check


def test_valid_sequence_returns_true():
    assert luhn_check("79927398713") is True


def test_invalid_check_digit_returns_false():
    assert luhn_check("79927398710") is False


def test_non_digit_input_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("7992739871a")


def test_over_1024_characters_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("1" * 1025)


def test_exactly_1024_digits_is_allowed():
    digits = "0" * 1024
    assert luhn_check(digits) is True
