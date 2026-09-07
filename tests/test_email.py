import pytest

from validkit.email import is_valid_email


@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "user.name+tag@example.co.uk",
        "USER@EXAMPLE.COM",
        "a@b.co",
        "first.last@sub.domain.example.com",
    ],
)
def test_valid_emails(email: str) -> None:
    assert is_valid_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "user@",
        "@example.com",
        "user@example",
        "user example.com",
        "user@@example.com",
        "user@example..com",
        ".user@example.com",
        "user.@example.com",
        "",
    ],
)
def test_invalid_emails(email: str) -> None:
    assert is_valid_email(email) is False


def test_email_at_1024_characters_boundary_is_allowed() -> None:
    local = "a" * (1024 - len("@example.com"))
    email = f"{local}@example.com"
    assert len(email) == 1024
    assert is_valid_email(email) is True


def test_email_over_1024_characters_raises_value_error() -> None:
    email = "a" * 1025 + "@example.com"
    with pytest.raises(ValueError):
        is_valid_email(email)
