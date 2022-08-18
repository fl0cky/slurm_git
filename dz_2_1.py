def my_range(stop: float, start=0.0, step=1.0) -> list[float]:
    result = []
    while start <= stop:
        result.append(start)
        start += step
    return result


print(my_range(10))
