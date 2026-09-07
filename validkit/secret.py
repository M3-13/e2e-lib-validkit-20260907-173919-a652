from validkit._validation import _check_length


def mask_secret(text: str, keep: int = 4) -> str:
    _check_length(text, what="text")

    if not isinstance(keep, int):
        raise TypeError("keep must be an integer")
    if keep < 0:
        raise ValueError("keep must be >= 0")

    if len(text) <= keep:
        return text

    if keep == 0:
        return "*" * len(text)

    return "*" * (len(text) - keep) + text[-keep:]
