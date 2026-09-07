import pytest

from validkit import normalize_phone


def test_normalizes_german_number():
    assert normalize_phone("030 1234567", "DE") == "+49301234567"


def test_strips_non_digit_characters():
    assert normalize_phone("(030) 1234-567", "DE") == "+49301234567"


def test_strips_leading_zeros_of_national_number():
    assert normalize_phone("0030 1234567", "DE") == "+49301234567"


def test_other_european_country_codes():
    assert normalize_phone("01 234 5678", "AT") == "+4312345678"
    assert normalize_phone("01 23 45 67 89", "FR") == "+33123456789"
    assert normalize_phone("044 123 45 67", "CH") == "+41441234567"


def test_lowercase_country_code():
    assert normalize_phone("030 1234567", "de") == "+49301234567"


def test_empty_digit_sequence_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("+++ --", "DE")


def test_unknown_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "ZZ")


def test_text_exceeding_1024_chars_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("1" * 1025, "DE")


def test_country_code_exceeding_1024_chars_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "D" * 1025)


def test_exactly_1024_chars_is_allowed():
    assert normalize_phone("1" * 1024, "DE") == "+49" + "1" * 1024


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(123456, "DE")


def test_non_string_country_code_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", 49)
