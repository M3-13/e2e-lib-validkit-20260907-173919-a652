from validkit._validation import _check_length


def luhn_check(digits: str) -> bool:
    _check_length(digits, what="digits")

    if not isinstance(digits, str):
        raise TypeError("digits must be a string")

    for char in digits:
        if not char.isdigit():
            raise ValueError("digits must contain only digit characters")

    total = 0
    double = False
    for char in reversed(digits):
        digit = int(char)
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        double = not double

    return total % 10 == 0
