import pytest

from moneykit.allocation import allocate


def test_a_bill_split_keep_every_cent():
    assert allocate(10000,[1,1,1]) == [3334, 3333, 3333]

def test_a_tie_cut_off():
    assert allocate(5, [3,7]) == [2,3]

def test_shares_follow_weights():
    assert allocate(1999, [1,2,3]) == [333,666,1000]

def test_with_no_weights():
    with pytest.raises(ValueError):
        assert allocate(10,[])

def test_with_negative_weights():
    with pytest.raises(ValueError):
        assert allocate(10,[-1])

