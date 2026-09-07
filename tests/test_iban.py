import pytest

from validkit.iban import is_valid_iban


def test_valid_german_iban() -> None:
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_iban_with_spaces_and_lowercase() -> None:
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_invalid_check_digits() -> None:
    assert is_valid_iban("DE99370400440532013000") is False


def test_invalid_bban_length() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("DE893704004405320130")


def test_invalid_country_code() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("12370400440532013000")


def test_invalid_check_digits_format() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("DEAB370400440532013000")


def test_unknown_country() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("XX89370400440532013000")


def test_invalid_bban_characters() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("DE8937040044053201300!")


def test_too_long_input() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("A" * 1025)


def test_exactly_1024_characters_is_checked_for_format() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("A" * 1024)
