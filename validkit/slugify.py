import re
import unicodedata

from validkit._validation import _check_length


def slugify(text: str) -> str:
    _check_length(text, what="text")

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")

    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower())
    slug = slug.strip("-")

    if not slug:
        raise ValueError("slugify result is empty")

    return slug
