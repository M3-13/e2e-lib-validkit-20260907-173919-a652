import unicodedata

from validkit._validation import _check_length


def strip_accents(text: str) -> str:
    _check_length(text, what="text")
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(char for char in decomposed if unicodedata.category(char) != "Mn")
