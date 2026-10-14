import pytest

from moneykit.errors import CurrencyMismatch, InvalidAmount
from moneykit.money import Money


def test_parse_dollars_as_cents():
    assert Money.parse("19.99", "USD").minor_units == 1999

def test_read_yen_with_no_decimal():
    assert Money.parse("1999", "JPY").minor_units == 1999

def test_adding_to_minor_units():
    total = Money.parse("19.99","USD") + Money.parse("0.01", "USD")
    assert total.minor_units == 2000

def test_display():
    assert str(Money.parse("19.99", "USD")) == "$19.99"
    assert str(Money.parse("1000", "JPY")) == "\u00a51,000"

def test_adding_currencies_raise_error():
    with pytest.raises(CurrencyMismatch):
        assert Money.parse("19.99", "USD") + Money.parse("1000", "JPY")

def test_over_decimals():
    with pytest.raises(InvalidAmount):
        assert Money.parse("19.999", "USD")

