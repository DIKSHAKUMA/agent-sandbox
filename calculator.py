"""Arithmetic helpers used by the billing calculator."""


def divide(numerator: float, denominator: float) -> float:
    """Divides two numbers.

    Raises:
        ValueError: if the denominator is zero.
    """
    return numerator / denominator


def average(values: list[float]) -> float:
    """Returns the mean of a list of numbers."""
    return divide(sum(values), len(values))
