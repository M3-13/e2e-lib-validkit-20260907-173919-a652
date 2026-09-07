from validkit._validation import _check_length


def is_valid_isbn13(text: str) -> bool:
    _check_length(text, what="text")

    digits = text.replace("-", "").replace(" ", "")

    if len(digits) != 13:
        raise ValueError("ISBN-13 must contain exactly 13 digits")

    if not digits.isdigit():
        raise ValueError("ISBN-13 must contain only digits")

    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))

    return total % 10 == 0
