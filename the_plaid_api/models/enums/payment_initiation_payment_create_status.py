from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInitiationPaymentCreateStatus(str, Enum):
    """For a payment returned by this endpoint, there is only one possible value:

    ``PAYMENT_STATUS_INPUT_NEEDED``: The initial phase of the payment"""

    PAYMENT_STATUS_INPUT_NEEDED = "PAYMENT_STATUS_INPUT_NEEDED"

    __str__ = str.__str__


PaymentInitiationPaymentCreateStatusOrStr: TypeAlias = Annotated[
    PaymentInitiationPaymentCreateStatus | str, open_enum_validator(PaymentInitiationPaymentCreateStatus)
]
