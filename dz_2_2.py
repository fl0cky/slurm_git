from typing import Generator


def my_range(stop: float, start=0.0, step=1.0) -> Generator[float]:
    while start <= stop:
        yield start
        start += step
