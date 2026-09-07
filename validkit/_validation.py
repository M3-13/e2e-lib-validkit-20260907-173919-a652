def _check_length(text: str, *, what: str) -> None:
    if len(text) > 1024:
        raise ValueError(f"{what} exceeds maximum length of 1024 characters")
