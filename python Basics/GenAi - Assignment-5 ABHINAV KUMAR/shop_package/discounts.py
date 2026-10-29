def apply_discount(price, percent):
    discounted_price = price*(percent/100)
    return price - discounted_price


def flat_discount(price):
    discount_price = price - 50 if price >= 50 else 0
    return price - discount_price

print(flat_discount(105))