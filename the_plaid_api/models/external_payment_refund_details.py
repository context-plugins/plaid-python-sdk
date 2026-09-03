from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .recipient_bacsnullable import RecipientBacsnullable, RecipientBacsnullableDict


class ExternalPaymentRefundDetails(SdkBaseModel):
    """Details about external payment refund"""

    name: str
    """The name of the account holder."""

    iban: str | None
    """The International Bank Account Number (IBAN) for the account."""

    bacs: RecipientBacsnullable | None
    """An object containing a Bacs account number and sort code. If an IBAN is not provided or if this recipient needs
    to accept domestic GBP-denominated payments, Bacs data is required."""


class ExternalPaymentRefundDetailsDict(TypedDict):
    name: str
    iban: str | None
    bacs: RecipientBacsnullable | RecipientBacsnullableDict | None
