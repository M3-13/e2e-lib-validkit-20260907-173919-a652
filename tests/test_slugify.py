import pytest

from validkit.slugify import slugify


def test_slugify_basic_example():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_lowercases_and_spaces():
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_accents():
    assert slugify("Crème brûlée") == "creme-brulee"


def test_slugify_collapses_multiple_hyphens():
    assert slugify("a  b   c") == "a-b-c"


def test_slugify_strips_leading_trailing_hyphens():
    assert slugify("-hello world-") == "hello-world"


def test_slugify_replaces_punctuation():
    assert slugify("Hello, World! How's it going?") == "hello-world-how-s-it-going"


def test_slugify_keeps_digits():
    assert slugify("Version 2.0") == "version-2-0"


def test_slugify_single_word():
    assert slugify("Hello") == "hello"


def test_slugify_umlauts_and_german():
    assert slugify("Über Öl und Äpfel") == "uber-ol-und-apfel"


def test_slugify_empty_string_raises():
    with pytest.raises(ValueError):
        slugify("")


def test_slugify_only_special_chars_raises():
    with pytest.raises(ValueError):
        slugify("!!!")


def test_slugify_whitespace_only_raises():
    with pytest.raises(ValueError):
        slugify("   ")


def test_slugify_wrong_type_raises():
    with pytest.raises(TypeError):
        slugify(123)  # type: ignore[arg-type]


def test_slugify_exactly_1024_chars_allowed():
    assert slugify("a" * 1024) == "a" * 1024


def test_slugify_more_than_1024_chars_raises():
    with pytest.raises(ValueError):
        slugify("a" * 1025)
