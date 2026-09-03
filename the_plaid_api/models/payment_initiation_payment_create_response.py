from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PaymentInitiationPaymentCreateResponse(SdkBaseModel):
    """PaymentInitiationPaymentCreateResponse defines the response schema for ``/payment_initiation/payment/create``"""

    payment_id: str
    """A unique ID identifying the payment"""

    status: Literal["PAYMENT_STATUS_INPUT_NEEDED"] = "PAYMENT_STATUS_INPUT_NEEDED"
    """For a payment returned by this endpoint, there is only one possible value:

    ``PAYMENT_STATUS_INPUT_NEEDED``: The initial phase of the payment"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationPaymentCreateResponseDict(TypedDict):
    payment_id: str
    status: NotRequired[Literal["PAYMENT_STATUS_INPUT_NEEDED"]]
    request_id: str
