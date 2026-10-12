from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.payment_initiation_consent_scope import PaymentInitiationConsentScopeOrStr
from .enums.payment_initiation_consent_status import PaymentInitiationConsentStatusOrStr
from .enums.payment_initiation_consent_type import PaymentInitiationConsentTypeOrStr
from .external_payment_refund_details import ExternalPaymentRefundDetails, ExternalPaymentRefundDetailsDict
from .payment_initiation_consent_constraints import (
    PaymentInitiationConsentConstraints,
    PaymentInitiationConsentConstraintsDict,
)


class PaymentInitiationConsent(SdkBaseModel):
    """PaymentInitiationConsent defines a payment initiation consent."""

    consent_id: str
    """The consent ID."""

    status: PaymentInitiationConsentStatusOrStr
    """The status of the payment consent.

    ``UNAUTHORISED``: Consent created, but requires user authorisation.

    ``REJECTED``: Consent authorisation was rejected by the bank.

    ``AUTHORISED``: Consent is active and ready to be used.

    ``REVOKED``: Consent has been revoked and can no longer be used.

    ``EXPIRED``: Consent is no longer valid."""

    created_at: RFC3339DateTime
    """Consent creation timestamp, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    recipient_id: str
    """The ID of the recipient the payment consent is for."""

    reference: str
    """A reference for the payment consent."""

    constraints: PaymentInitiationConsentConstraints
    """Limitations that will be applied to payments initiated using the payment consent."""

    scopes: Optional[list[PaymentInitiationConsentScopeOrStr]] = UNSET
    """Deprecated, use the 'type' field instead."""

    type_: Optional[PaymentInitiationConsentTypeOrStr] = Field(default=UNSET, alias="type")
    """Payment consent type. Defines possible use case for payments made with the given consent.

    ``SWEEPING``: Allows moving money between accounts owned by the same user.

    ``COMMERCIAL``: Allows initiating payments from the user's account to third parties."""

    payer_details: OptionalNullable[ExternalPaymentRefundDetails] = UNSET
    """Details about external payment refund"""


class PaymentInitiationConsentDict(TypedDict):
    consent_id: str
    status: PaymentInitiationConsentStatusOrStr
    created_at: RFC3339DateTime
    recipient_id: str
    reference: str
    constraints: PaymentInitiationConsentConstraintsDict
    scopes: NotRequired[list[PaymentInitiationConsentScopeOrStr]]
    type_: NotRequired[PaymentInitiationConsentTypeOrStr]
    payer_details: NotRequired[ExternalPaymentRefundDetailsDict | None]
