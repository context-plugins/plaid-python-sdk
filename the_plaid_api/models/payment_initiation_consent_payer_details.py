from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict
from .payment_initiation_consent_payer_numbers import (
    PaymentInitiationConsentPayerNumbers,
    PaymentInitiationConsentPayerNumbersDict,
)


class PaymentInitiationConsentPayerDetails(SdkBaseModel):
    """An object representing the payment consent payer details. Payer ``name`` and account ``numbers`` are required to
    lock the account to which the consent can be created."""

    name: str
    """The name of the payer as it appears in their bank account"""

    numbers: PaymentInitiationConsentPayerNumbers
    """The payer's bank account numbers. Exactly one of IBAN or Bacs data is required."""

    address: OptionalNullable[PaymentInitiationAddress] = UNSET
    """The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""

    date_of_birth: OptionalNullable[Date] = UNSET
    """The payer's birthdate, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format."""

    phone_numbers: Optional[list[str]] = UNSET
    """The payer's phone numbers in E.164 format: +{countrycode}{number}"""

    emails: Optional[list[str]] = UNSET
    """The payer's emails"""


class PaymentInitiationConsentPayerDetailsDict(TypedDict):
    name: str
    numbers: PaymentInitiationConsentPayerNumbers | PaymentInitiationConsentPayerNumbersDict
    address: NotRequired[PaymentInitiationAddress | PaymentInitiationAddressDict | None]
    date_of_birth: NotRequired[Date | None]
    phone_numbers: NotRequired[list[str]]
    emails: NotRequired[list[str]]
