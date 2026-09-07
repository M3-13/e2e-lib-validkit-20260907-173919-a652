import pytest

from validkit import clamp


def test_clamp_value_within_bounds() -> None:
    assert clamp(5, 0, 10) == 5


def test_clamp_value_below_lower_bound() -> None:
    assert clamp(-3, 0, 10) == 0


def test_clamp_value_above_upper_bound() -> None:
    assert clamp(15, 0, 10) == 10


def test_clamp_lower_bound() -> None:
    assert clamp(0, 0, 10) == 0


def test_clamp_upper_bound() -> None:
    assert clamp(10, 0, 10) == 10


def test_clamp_equal_bounds() -> None:
    assert clamp(7, 5, 5) == 5


def test_clamp_low_greater_than_high_raises() -> None:
    with pytest.raises(ValueError):
        clamp(0, 5, 1)
