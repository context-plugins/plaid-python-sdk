from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .payment_amount_to_refund import PaymentAmountToRefund, PaymentAmountToRefundDict
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict


class PaymentInitiationPaymentReverseRequest(SdkBaseModel):
    """PaymentInitiationPaymentReverseRequest defines the request schema for ``/payment_initiation/payment/reverse``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    payment_id: str
    """The ID of the payment to reverse"""

    idempotency_key: str
    """A random key provided by the client, per unique wallet transaction. Maximum of 128 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    If a request to execute a wallet transaction fails due to a network connection error, then after a minimum delay of
    one minute, you can retry the request with the same idempotency key to guarantee that only a single wallet
    transaction is created. If the request was successfully processed, it will prevent any transaction that uses the
    same idempotency key, and was received within 24 hours of the first request, from being processed."""

    reference: str
    """A reference for the refund. This must be an alphanumeric string with 6 to 18 characters and must not contain any
    special characters or spaces."""

    amount: OptionalNullable[PaymentAmountToRefund] = UNSET
    """The amount and currency of a payment"""

    counterparty_date_of_birth: OptionalNullable[Date] = UNSET
    """The counterparty's birthdate, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format."""

    counterparty_address: OptionalNullable[PaymentInitiationAddress] = UNSET
    """The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""


class PaymentInitiationPaymentReverseRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    payment_id: str
    idempotency_key: str
    reference: str
    amount: NotRequired[PaymentAmountToRefundDict | None]
    counterparty_date_of_birth: NotRequired[Date | None]
    counterparty_address: NotRequired[PaymentInitiationAddressDict | None]
