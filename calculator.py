"""Arithmetic helpers used by the billing calculator."""


def divide(numerator: float, denominator: float) -> float:
    """Divides two numbers.

    Raises:
        ValueError: if the denominator is zero.
    """
    if denominator == 0:
        raise ValueError("denominator must not be zero")

    return numerator / denominator


def average(values: list[float]) -> float:
    """Returns the mean of a list of numbers."""
    return divide(sum(values), len(values))
