import pytest

from validkit import strip_accents


def test_strips_accents_from_combined_words():
    assert strip_accents("café naïve") == "cafe naive"


def test_strips_german_umlauts():
    assert strip_accents("München Köln") == "Munchen Koln"


def test_strips_various_latin_accents():
    assert strip_accents("àéîõüçñ") == "aeioucn"


def test_plain_ascii_is_unchanged():
    assert strip_accents("hello world") == "hello world"


def test_empty_string():
    assert strip_accents("") == ""


def test_no_accents_to_strip():
    assert strip_accents("plain text 123") == "plain text 123"


def test_strips_precomposed_into_separate_chars():
    assert strip_accents("Ångström résumé") == "Angstrom resume"


def test_mixed_accents_and_non_accents():
    assert strip_accents("naïve café déjà vu") == "naive cafe deja vu"


def test_allows_exactly_1024_chars():
    text = "café" * 256
    assert len(text) == 1024
    result = strip_accents(text)
    assert result == "cafe" * 256


def test_rejects_more_than_1024_chars():
    with pytest.raises(ValueError) as exc_info:
        strip_accents("é" * 1025)
    assert "text" in str(exc_info.value)


def test_rejects_non_string():
    with pytest.raises(TypeError):
        strip_accents(12345)


def test_rejects_none():
    with pytest.raises(TypeError):
        strip_accents(None)
