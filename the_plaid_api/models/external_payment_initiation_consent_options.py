from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .payment_initiation_optional_restriction_bacs import (
    PaymentInitiationOptionalRestrictionBacs,
    PaymentInitiationOptionalRestrictionBacsDict,
)


class ExternalPaymentInitiationConsentOptions(SdkBaseModel):
    """(Deprecated) Additional payment consent options. Please use ``payer_details`` to specify the account."""

    request_refund_details: OptionalNullable[bool] = UNSET
    """When ``true``, Plaid will attempt to request refund details from the payee's financial institution. Support
    varies between financial institutions and will not always be available. If refund details could be retrieved, they
    will be available in the ``/payment_initiation/payment/get`` response."""

    iban: OptionalNullable[str] = UNSET
    """The International Bank Account Number (IBAN) for the payer's account. Where possible, the end user will be able
    to set up payment consent using only the specified bank account if provided."""

    bacs: OptionalNullable[PaymentInitiationOptionalRestrictionBacs] = UNSET
    """An optional object used to restrict the accounts used for payments. If provided, the end user will be able to
    send payments only from the specified bank account."""


class ExternalPaymentInitiationConsentOptionsDict(TypedDict):
    request_refund_details: NotRequired[bool | None]
    iban: NotRequired[str | None]
    bacs: NotRequired[PaymentInitiationOptionalRestrictionBacs | PaymentInitiationOptionalRestrictionBacsDict | None]
