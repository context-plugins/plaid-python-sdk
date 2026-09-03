from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SignalPaymentMethod(str, Enum):
    """The payment method to complete the transaction after the risk assessment. It may be different from the default
    payment method.

    ``SAME_DAY_ACH``: Same Day ACH by Nacha. The debit transaction is processed and settled on the same day.

    ``STANDARD_ACH``: Standard ACH by Nacha.

    ``MULTIPLE_PAYMENT_METHODS``: if there is no default debit rail or there are multiple payment methods."""

    SAME_DAY_ACH = "SAME_DAY_ACH"
    NEXT_DAY_ACH = "NEXT_DAY_ACH"
    STANDARD_ACH = "STANDARD_ACH"
    MULTIPLE_PAYMENT_METHODS = "MULTIPLE_PAYMENT_METHODS"

    __str__ = str.__str__


SignalPaymentMethodOrStr: TypeAlias = Annotated[SignalPaymentMethod | str, open_enum_validator(SignalPaymentMethod)]
