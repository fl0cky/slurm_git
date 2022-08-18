def chain_sum(value: int = None):
    result = getattr(chain_sum, "result", 0)
    if value is None:
        chain_sum.result = 0
        return result
    chain_sum.result = value + result

    return chain_sum
