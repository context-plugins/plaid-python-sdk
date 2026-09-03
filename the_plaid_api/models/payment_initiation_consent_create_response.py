from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.payment_initiation_consent_status import PaymentInitiationConsentStatusOrStr


class PaymentInitiationConsentCreateResponse(SdkBaseModel):
    """PaymentInitiationConsentCreateResponse defines the response schema for ``/payment_initiation/consent/create``"""

    consent_id: str
    """A unique ID identifying the payment consent."""

    status: PaymentInitiationConsentStatusOrStr
    """The status of the payment consent.

    ``UNAUTHORISED``: Consent created, but requires user authorisation.

    ``REJECTED``: Consent authorisation was rejected by the bank.

    ``AUTHORISED``: Consent is active and ready to be used.

    ``REVOKED``: Consent has been revoked and can no longer be used.

    ``EXPIRED``: Consent is no longer valid."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationConsentCreateResponseDict(TypedDict):
    consent_id: str
    status: PaymentInitiationConsentStatusOrStr
    request_id: str
