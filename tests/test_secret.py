import pytest

from validkit.secret import mask_secret


def test_keep_zero_masks_everything():
    assert mask_secret("abcdefgh", keep=0) == "********"


def test_keep_equal_to_length_returns_text_unchanged():
    assert mask_secret("abcdefgh", keep=8) == "abcdefgh"


def test_keep_greater_than_length_returns_text_unchanged():
    assert mask_secret("abcdefgh", keep=100) == "abcdefgh"


def test_keep_four_masks_prefix():
    assert mask_secret("abcdefgh", keep=4) == "****efgh"


def test_default_keep_is_four():
    assert mask_secret("abcdefgh") == "****efgh"


def test_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("abcdefgh", keep=-1)


def test_non_integer_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("abcdefgh", keep="4")  # type: ignore[arg-type]


def test_float_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("abcdefgh", keep=4.0)  # type: ignore[arg-type]


def test_more_than_1024_chars_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("a" * 1025, keep=4)


def test_exactly_1024_chars_is_allowed():
    assert len(mask_secret("a" * 1024, keep=0)) == 1024


@pytest.mark.parametrize(
    "secret",
    [
        "S3cr3t!Value",
        "super-geheimer-inhalt",
        "password123",
        "topsecret",
    ],
)
def test_error_messages_do_not_contain_plaintext(secret):
    with pytest.raises((ValueError, TypeError)) as excinfo:
        mask_secret(secret, keep=-1)
    assert secret not in str(excinfo.value)


def test_non_integer_keep_message_does_not_contain_plaintext():
    secret = "geheimer-wert"
    with pytest.raises(TypeError) as excinfo:
        mask_secret(secret, keep="x")  # type: ignore[arg-type]
    assert secret not in str(excinfo.value)
