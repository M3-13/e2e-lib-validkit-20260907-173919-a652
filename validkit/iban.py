import re

from validkit._validation import _check_length

_BBAN_LENGTHS: dict[str, int] = {
    "AL": 24,
    "AD": 20,
    "AT": 16,
    "AZ": 24,
    "BH": 18,
    "BE": 12,
    "BA": 16,
    "BR": 25,
    "BG": 18,
    "CR": 18,
    "HR": 17,
    "CY": 24,
    "CZ": 20,
    "DK": 14,
    "DO": 24,
    "TL": 19,
    "EE": 16,
    "FO": 14,
    "FI": 14,
    "FR": 23,
    "GE": 18,
    "DE": 18,
    "GI": 19,
    "GR": 23,
    "GL": 14,
    "GT": 24,
    "HU": 24,
    "IS": 22,
    "IE": 18,
    "IL": 19,
    "IT": 23,
    "JO": 26,
    "KZ": 16,
    "XK": 16,
    "KW": 26,
    "LV": 17,
    "LB": 24,
    "LI": 17,
    "LT": 16,
    "LU": 16,
    "MK": 15,
    "MT": 27,
    "MR": 23,
    "MU": 26,
    "MD": 20,
    "MC": 23,
    "ME": 18,
    "NL": 14,
    "NO": 11,
    "PK": 20,
    "PS": 25,
    "PL": 24,
    "PT": 21,
    "QA": 25,
    "RO": 20,
    "SM": 23,
    "SA": 20,
    "RS": 18,
    "SK": 20,
    "SI": 15,
    "ES": 20,
    "SE": 20,
    "CH": 17,
    "TN": 20,
    "TR": 22,
    "UA": 25,
    "AE": 19,
    "GB": 18,
    "VA": 18,
    "VG": 20,
}


def is_valid_iban(text: str) -> bool:
    _check_length(text, what="text")

    normalized = text.replace(" ", "").upper()

    if len(normalized) < 4:
        raise ValueError("IBAN must start with a country code and check digits")

    country = normalized[:2]
    check_digits = normalized[2:4]
    bban = normalized[4:]

    if not re.fullmatch(r"[A-Z]{2}", country):
        raise ValueError(f"invalid country code: {country!r}")
    if not re.fullmatch(r"[0-9]{2}", check_digits):
        raise ValueError(f"invalid check digits: {check_digits!r}")

    expected_len = _BBAN_LENGTHS.get(country)
    if expected_len is None:
        raise ValueError(f"unsupported country code: {country!r}")

    if len(bban) != expected_len:
        raise ValueError(
            f"invalid BBAN length for {country}: expected {expected_len} "
            f"characters, got {len(bban)}"
        )

    if not re.fullmatch(r"[A-Z0-9]+", bban):
        raise ValueError("BBAN must contain only letters and digits")

    rearranged = bban + country + check_digits
    digits = "".join(str(ord(char) - 55) if char.isalpha() else char for char in rearranged)

    return int(digits) % 97 == 1
