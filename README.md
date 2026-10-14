# MoneyKit


MoneyKit is a small Python library for working with money safely and splitting amounts fairly.

## Install

```bash
pip install git+https://github.com
```

## Example

```python
from moneykit.money import Money
from moneykit.allocation import allocate

price = Money.parse("19.99", "USD")
print(price + Money.parse("0.01", "USD"))  # \$20.00
print(allocate(10000, [1, 1, 1]))            # [3334, 3333, 3333]
```

MoneyKit supports currencies with different decimal places and prevents adding amounts in different currencies. The allocate function splits an integer amount by weights without losing any units.

## Run Tests

To run the complete test suite locally:
```powershell
\$env:PYTHONPATH="src"; pytest -q
```

To check code style, static types, and exact test coverage metrics:
```powershell
ruff check .
mypy src/moneykit --strict
\$env:PYTHONPATH="src"; pytest -q --cov=moneykit --cov-report=term-missing
```

## What it does not do yet

- Convert money between currencies or get exchange rates.
- Connect to banks or process payments.
- Split amounts directly into Money objects; allocation currently works with integers.
