from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.payment_amount_currency import PaymentAmountCurrencyOrStr


class PaymentAmount(SdkBaseModel):
    """The amount and currency of a payment"""

    currency: PaymentAmountCurrencyOrStr
    """The ISO-4217 currency code of the payment. For standing orders and payment consents, ``"GBP"`` must be used. For
    Poland, Denmark, Sweden and Norway, only the local currency is currently supported."""

    value: float
    """The amount of the payment. Must contain at most two digits of precision e.g. ``1.23``. Minimum accepted value is
    ``1``."""


class PaymentAmountDict(TypedDict):
    currency: PaymentAmountCurrencyOrStr
    value: float
