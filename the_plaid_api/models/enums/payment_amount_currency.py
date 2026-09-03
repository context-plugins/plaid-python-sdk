from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentAmountCurrency(str, Enum):
    """The ISO-4217 currency code of the payment. For standing orders and payment consents, ``"GBP"`` must be used. For
    Poland, Denmark, Sweden and Norway, only the local currency is currently supported."""

    GBP = "GBP"
    EUR = "EUR"
    PLN = "PLN"
    SEK = "SEK"
    DKK = "DKK"
    NOK = "NOK"

    __str__ = str.__str__


PaymentAmountCurrencyOrStr: TypeAlias = Annotated[
    PaymentAmountCurrency | str, open_enum_validator(PaymentAmountCurrency)
]
