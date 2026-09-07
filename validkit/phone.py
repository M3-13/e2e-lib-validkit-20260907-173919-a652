from validkit._validation import _check_length

_COUNTRY_CALLING_CODES = {
    "AT": "43",
    "BE": "32",
    "BG": "359",
    "CH": "41",
    "CZ": "420",
    "DE": "49",
    "DK": "45",
    "EE": "372",
    "ES": "34",
    "FI": "358",
    "FR": "33",
    "GB": "44",
    "GR": "30",
    "HR": "385",
    "HU": "36",
    "IE": "353",
    "IT": "39",
    "LT": "370",
    "LU": "352",
    "LV": "371",
    "NL": "31",
    "NO": "47",
    "PL": "48",
    "PT": "351",
    "RO": "40",
    "SE": "46",
    "SI": "386",
    "SK": "421",
}


def normalize_phone(text: str, country_code: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a string")

    _check_length(text, what="text")
    _check_length(country_code, what="country_code")

    calling_code = _COUNTRY_CALLING_CODES.get(country_code.upper())
    if calling_code is None:
        raise ValueError(f"unknown country code {country_code!r}")

    digits = "".join(ch for ch in text if ch.isdigit()).lstrip("0")
    if not digits:
        raise ValueError("phone number contains no digits")

    return f"+{calling_code}{digits}"
