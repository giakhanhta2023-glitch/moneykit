from dataclasses import dataclass


@dataclass(frozen=True)
class Currency:
    code: str           # "USD"
    exponent: int       # 2
    symbol: str = ""

CURRENCIES = {
    "USD": Currency("USD", 2, "$"),
    "EUR": Currency("EUR", 2, "\u20ac"),
    "GBP": Currency("GBP", 2, "\u00a3"),
    "JPY": Currency("JPY", 0, "\u00a5"),
    "VND": Currency("VND", 0, "\u20ab"),
    "BHD": Currency("BHD", 3, ""),
}