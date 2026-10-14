from hypothesis import given
from hypothesis import strategies as st

from moneykit.allocation import allocate
from moneykit.currency import CURRENCIES
from moneykit.money import Money

amounts = st.integers(min_value = 0, max_value = 10**12)
weights_list = st.lists(st.integers(min_value = 0, max_value = 10**12),min_size =1, max_size=12 )

@given(total = amounts, weights = weights_list)
def test_sum_shares_equal_total(total, weights):
    assert sum(allocate(amounts, weights_list)) == allocate(amounts, weights_list)

@given(total = amounts, weights = weights_list)
def test_allocation_not_random(total, weights):
    assert allocate(amounts, weights_list) == allocate(amounts, weights_list)

@given(a = amounts, b = amounts)
def test_add_then_subtract_equal_original(a,b):
    usd = CURRENCIES["USD"]
    assert (Money(a,usd) + Money(b,usd)) - Money(b,usd)  == Money(a,usd)


