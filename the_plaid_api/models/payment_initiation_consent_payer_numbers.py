from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .payment_initiation_optional_restriction_bacs import (
    PaymentInitiationOptionalRestrictionBacs,
    PaymentInitiationOptionalRestrictionBacsDict,
)


class PaymentInitiationConsentPayerNumbers(SdkBaseModel):
    """The payer's bank account numbers. Exactly one of IBAN or Bacs data is required."""

    bacs: OptionalNullable[PaymentInitiationOptionalRestrictionBacs] = UNSET
    """An optional object used to restrict the accounts used for payments. If provided, the end user will be able to
    send payments only from the specified bank account."""

    iban: OptionalNullable[str] = UNSET
    """International Bank Account Number (IBAN)."""


class PaymentInitiationConsentPayerNumbersDict(TypedDict):
    bacs: NotRequired[PaymentInitiationOptionalRestrictionBacs | PaymentInitiationOptionalRestrictionBacsDict | None]
    iban: NotRequired[str | None]
