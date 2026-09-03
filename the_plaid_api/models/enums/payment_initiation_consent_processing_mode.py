from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInitiationConsentProcessingMode(str, Enum):
    """Decides the mode under which the payment processing should be performed, using ``IMMEDIATE`` as default.

    ``IMMEDIATE``: Will immediately execute the payment, waiting for a response from the ASPSP before returning the
    result of the payment initiation. This is ideal for user-present flows.

     ``ASYNC``: Will accept a payment execution request and schedule it for processing, immediately returning the new
        ``payment_id``. Listen for webhooks to obtain real-time updates on the payment status. This is ideal for non
        user-present flows."""

    ASYNC = "ASYNC"
    IMMEDIATE = "IMMEDIATE"

    __str__ = str.__str__


PaymentInitiationConsentProcessingModeOrStr: TypeAlias = Annotated[
    PaymentInitiationConsentProcessingMode | str, open_enum_validator(PaymentInitiationConsentProcessingMode)
]
