from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.payment_initiation_consent_processing_mode import PaymentInitiationConsentProcessingModeOrStr
from .enums.payment_initiation_consent_scope import PaymentInitiationConsentScopeOrStr
from .payment_amount import PaymentAmount, PaymentAmountDict


class PaymentInitiationConsentPaymentExecuteRequest(SdkBaseModel):
    """PaymentInitiationConsentPaymentExecuteRequest defines the request schema for
    ``/payment_initiation/consent/payment/execute``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    consent_id: str
    """The consent ID."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    idempotency_key: str
    """A random key provided by the client, per unique consent payment. Maximum of 128 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    If a request to execute a consent payment fails due to a network connection error, you can retry the request with
    the same idempotency key to guarantee that only a single payment is created. If the request was successfully
    processed, it will prevent any payment that uses the same idempotency key, and was received within 48 hours of the
    first request, from being processed."""

    reference: OptionalNullable[str] = UNSET
    """A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain
    any special characters (since not all institutions support them). If not provided, Plaid will automatically fall
    back to the reference from consent. In order to track settlement via Payment Confirmation, each payment must have a
    unique reference. If the reference provided through the API is not unique, Plaid will adjust it. Some institutions
    may limit the reference to less than 18 characters. If necessary, Plaid will adjust the reference by truncating it
    to fit the institution's requirements. Both the originally provided and automatically adjusted references (if any)
    can be found in the ``reference`` and ``adjusted_reference`` fields, respectively."""

    scope: OptionalNullable[PaymentInitiationConsentScopeOrStr] = UNSET
    processing_mode: Optional[PaymentInitiationConsentProcessingModeOrStr] = UNSET
    """Decides the mode under which the payment processing should be performed, using ``IMMEDIATE`` as default.

    ``IMMEDIATE``: Will immediately execute the payment, waiting for a response from the ASPSP before returning the
    result of the payment initiation. This is ideal for user-present flows.

     ``ASYNC``: Will accept a payment execution request and schedule it for processing, immediately returning the new
        ``payment_id``. Listen for webhooks to obtain real-time updates on the payment status. This is ideal for non
        user-present flows."""


class PaymentInitiationConsentPaymentExecuteRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    consent_id: str
    amount: PaymentAmountDict
    idempotency_key: str
    reference: NotRequired[str | None]
    scope: NotRequired[PaymentInitiationConsentScopeOrStr | None]
    processing_mode: NotRequired[PaymentInitiationConsentProcessingModeOrStr]
