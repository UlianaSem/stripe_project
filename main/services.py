import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_stripe_session(price, name, path, tax=None, discount=None, currency="rub"):
    price_id = stripe.Price.create(
        currency=currency,
        unit_amount=price,
        product_data={"name": name},
    ).id

    body = {
        "success_url": f"{path}success/",
        "cancel_url": f"{path}cancel/",
        "line_items": [{"price": price_id, "quantity": 1}],
        "mode": "payment",
            }

    if discount:
        body["discounts"] = [{"coupon": discount}]

    if tax:
        body["line_items"][0]["tax_rates"] = [tax]

    session = stripe.checkout.Session.create(**body)

    return session.id


def create_stripe_discount(percent):
    discount = stripe.Coupon.create(
        duration="repeating",
        duration_in_months=3,
        percent_off=percent,
    )

    return discount.id


def create_stripe_tax(percent):
    tax = stripe.TaxRate.create(
        display_name="VAT",
        description="VAT",
        percentage=percent,
        jurisdiction="RU",
        inclusive=False,
    )

    return tax.id
