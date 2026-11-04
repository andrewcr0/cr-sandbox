"""Small arithmetic helpers."""


def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def average(values: list[float]) -> float:
    if not values:
        raise ValueError("average of empty list")
    return sum(values) / len(values)
