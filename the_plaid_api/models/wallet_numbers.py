from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .numbers_international_iban import NumbersInternationalIban, NumbersInternationalIbanDict
from .recipient_bacs import RecipientBacs, RecipientBacsDict


class WalletNumbers(SdkBaseModel):
    """An object representing the e-wallet account numbers"""

    bacs: OptionalNullable[RecipientBacs] = UNSET
    """An object containing a Bacs account number and sort code. If an IBAN is not provided or if you need to accept
    domestic GBP-denominated payments, Bacs data is required."""

    international: OptionalNullable[NumbersInternationalIban] = UNSET
    """Account numbers using the International Bank Account Number and BIC/SWIFT code format."""


class WalletNumbersDict(TypedDict):
    bacs: NotRequired[RecipientBacsDict | None]
    international: NotRequired[NumbersInternationalIbanDict | None]
