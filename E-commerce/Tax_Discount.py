TAX_RATES = {
    'NY': 8.875,
    'CA': 7.25,
    'TX': 6.25,
    'FL': 6.0,
    'DEFAULT': 5.0,
}

# Available coupon codes and their percentage discounts
COUPONS = {
    'WELCOME10': 10,
    'VIP20': 20,
    'FIVEOFF': 5,
}


def get_tax_rate(location: str) -> float:
    if not location:
        return TAX_RATES['DEFAULT']
    key = location.strip().upper()
    return TAX_RATES.get(key, TAX_RATES['DEFAULT'])


def compute_total(subtotal: float, location: str, coupon: str = None) -> dict:
    """Compute final total using coupons only (no tier/subtotal discounts).

    Returns a dict with details for display.
    """
    subtotal = max(0.0, float(subtotal))
    coupon_discount = 0.0
    coupon_valid = False
    if coupon:
        code = coupon.strip().upper()
        if code in COUPONS:
            coupon_discount = COUPONS[code]
            coupon_valid = True
        else:
            coupon_valid = False

    # Only coupon discounts apply
    total_discount = coupon_discount if coupon_valid else 0.0

    # cap total discount to 50%
    if total_discount > 50:
        total_discount = 50.0

    discount_total = subtotal * (1.0 - (total_discount / 100.0))
    tax_rate = get_tax_rate(location)
    taxed_total = discount_total * (1.0 + (tax_rate / 100.0))

    return {
        'subtotal': subtotal,
        'tier_discount': 0.0,
        'coupon_discount': coupon_discount if coupon_valid else 0.0,
        'coupon_valid': coupon_valid,
        'total_discount_percent': total_discount,
        'discounted_total': round(discount_total, 2),
        'tax_rate_percent': tax_rate,
        'final_total': round(taxed_total, 2),
    }


if __name__ == '__main__':
    print('Tax and Discount module loaded.')
