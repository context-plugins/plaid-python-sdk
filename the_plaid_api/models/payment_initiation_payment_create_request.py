from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .external_payment_schedule_request import ExternalPaymentScheduleRequest, ExternalPaymentScheduleRequestDict
from .payment_amount import PaymentAmount, PaymentAmountDict
from .payment_options import PaymentOptions, PaymentOptionsDict


class PaymentInitiationPaymentCreateRequest(SdkBaseModel):
    """PaymentInitiationPaymentCreateRequest defines the request schema for ``/payment_initiation/payment/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    recipient_id: str
    """The ID of the recipient the payment is for."""

    reference: str
    """A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain
    any special characters (since not all institutions support them). In order to track settlement via Payment
    Confirmation, each payment must have a unique reference. If the reference provided through the API is not unique,
    Plaid will adjust it. Some institutions may limit the reference to less than 18 characters. If necessary, Plaid will
    adjust the reference by truncating it to fit the institution's requirements. Both the originally provided and
    automatically adjusted references (if any) can be found in the ``reference`` and ``adjusted_reference`` fields,
    respectively."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    schedule: OptionalNullable[ExternalPaymentScheduleRequest] = UNSET
    """The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up
    as a standing order. If no schedule is specified, the payment will be executed only once."""

    options: OptionalNullable[PaymentOptions] = UNSET
    """Additional payment options"""


class PaymentInitiationPaymentCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    recipient_id: str
    reference: str
    amount: PaymentAmountDict
    schedule: NotRequired[ExternalPaymentScheduleRequestDict | None]
    options: NotRequired[PaymentOptionsDict | None]
