from dz_2_3 import chain_sum


def test_chain():
    assert chain_sum(10)()
    assert chain_sum(5)()
    assert chain_sum(20)()

test_chain()