import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_stripe_session(price, name):
    price_id = stripe.Price.create(
        currency="rub",
        unit_amount=price,
        product_data={"name": name},
    ).id

    session = stripe.checkout.Session.create(
      success_url="https://example.com/success",
      line_items=[{"price": price_id, "quantity": 1}],
      mode="payment",
    )

    return session.id
