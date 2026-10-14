from dataclasses import dataclass
from decimal import Decimal

from moneykit.currency import CURRENCIES, Currency
from moneykit.errors import CurrencyMismatch, InvalidAmount


@dataclass
class Money:
    minor_units : int
    currency : Currency

    @classmethod
    def parse(cls, text : str, code : str) -> "Money":
        cur = CURRENCIES[code]
        scaled = Decimal(text)*(10**cur.exponent)
        if scaled != scaled.to_integral_value():
            raise InvalidAmount(f"{text} has more decimal places than {cur.code} allows")
        return cls(int(scaled), cur)

    def _same_currency(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise CurrencyMismatch(f"{self.currency.code} and {other.currency.code}")

    def __add__(self, other: "Money") -> "Money":
        self._same_currency(other)
        return Money(self.minor_units + other.minor_units, self.currency)

    def __sub__(self, other: "Money") -> "Money":
        self._same_currency(other)
        return Money(self.minor_units - other.minor_units, self.currency)

    def __str__(self) -> str:
        units = Decimal(self.minor_units)/(10**self.currency.exponent)
        return f"{self.currency.symbol}{units:,.{self.currency.exponent}f}"

print(Money.parse("19.99", "USD")+ Money.parse("0.01", "USD"))



