def clamp(value: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError(f"low ({low}) must not be greater than high ({high})")
    return max(low, min(value, high))
