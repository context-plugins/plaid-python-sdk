from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.payment_initiation_consent_scope import PaymentInitiationConsentScopeOrStr
from .enums.payment_initiation_consent_type import PaymentInitiationConsentTypeOrStr
from .external_payment_initiation_consent_options import (
    ExternalPaymentInitiationConsentOptions,
    ExternalPaymentInitiationConsentOptionsDict,
)
from .payment_initiation_consent_constraints import (
    PaymentInitiationConsentConstraints,
    PaymentInitiationConsentConstraintsDict,
)
from .payment_initiation_consent_payer_details import (
    PaymentInitiationConsentPayerDetails,
    PaymentInitiationConsentPayerDetailsDict,
)


class PaymentInitiationConsentCreateRequest(SdkBaseModel):
    """PaymentInitiationConsentCreateRequest defines the request schema for ``/payment_initiation/consent/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    recipient_id: str
    """The ID of the recipient the payment consent is for. The created consent can be used to transfer funds to this
    recipient only."""

    reference: str
    """A reference for the payment consent. This must be an alphanumeric string with at most 18 characters and must not
    contain any special characters."""

    scopes: Optional[list[PaymentInitiationConsentScopeOrStr]] = UNSET
    """An array of payment consent scopes."""

    type_: Optional[PaymentInitiationConsentTypeOrStr] = Field(default=UNSET, alias="type")
    """Payment consent type. Defines possible use case for payments made with the given consent.

    ``SWEEPING``: Allows moving money between accounts owned by the same user.

    ``COMMERCIAL``: Allows initiating payments from the user's account to third parties."""

    constraints: PaymentInitiationConsentConstraints
    """Limitations that will be applied to payments initiated using the payment consent."""

    options: OptionalNullable[ExternalPaymentInitiationConsentOptions] = UNSET
    """(Deprecated) Additional payment consent options. Please use ``payer_details`` to specify the account."""

    payer_details: OptionalNullable[PaymentInitiationConsentPayerDetails] = UNSET
    """An object representing the payment consent payer details. Payer ``name`` and account ``numbers`` are required to
    lock the account to which the consent can be created."""


class PaymentInitiationConsentCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    recipient_id: str
    reference: str
    scopes: NotRequired[list[PaymentInitiationConsentScopeOrStr]]
    type_: NotRequired[PaymentInitiationConsentTypeOrStr]
    constraints: PaymentInitiationConsentConstraints | PaymentInitiationConsentConstraintsDict
    options: NotRequired[ExternalPaymentInitiationConsentOptions | ExternalPaymentInitiationConsentOptionsDict | None]
    payer_details: NotRequired[PaymentInitiationConsentPayerDetails | PaymentInitiationConsentPayerDetailsDict | None]
