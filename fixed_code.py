```python
import collections.abc
from decimal import Decimal

def calculate_total(items):
    # 2. Add initial input validation
    if not isinstance(items, collections.abc.Iterable):
        raise TypeError("Items must be an iterable.")

    # 3. Initialize the total accumulator as Decimal(0)
    total = Decimal(0)

    for item in items:
        try:
            # 4. Wrap attribute access (`item.price`, `item.quantity`) in a try-except AttributeError block.
            item_price_value = item.price
            item_quantity_value = item.quantity

            try:
                # 5. Within the `try` block (for attribute access), convert `item.price` and `item.quantity`
                # to `Decimal` objects. Wrap this conversion and subsequent multiplication/addition
                # in a nested `try-except TypeError` block to handle non-numeric values.
                price_decimal = Decimal(item_price_value)
                quantity_decimal = Decimal(item_quantity_value)

                # 6. Perform all arithmetic operations (multiplication and addition to `total`)
                # using `Decimal` objects to maintain precision.
                total += price_decimal * quantity_decimal
            except TypeError:
                # Handle non-numeric values that cause TypeError during Decimal conversion
                # (e.g., item.price is None or an object not convertible to decimal).
                # Skipping this item's contribution as it's malformed for calculation.
                continue
        except AttributeError:
            # Handle cases where `item` is missing `price` or `quantity` attributes.
            # Skipping this item's contribution as it's malformed for calculation.
            continue

    return total
```