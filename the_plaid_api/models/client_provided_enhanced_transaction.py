from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enhancements import Enhancements, EnhancementsDict


class ClientProvidedEnhancedTransaction(SdkBaseModel):
    """A client-provided transaction that Plaid has enhanced."""

    id: str
    """Unique transaction identifier to tie transactions back to clients' systems."""

    description: str
    """The raw description of the transaction."""

    amount: float
    """The value of the transaction, denominated in the account's currency, as stated in ``iso_currency_code``. Positive
    values when money moves out of the account; negative values when money moves in. For example, debit card purchases
    are positive; credit card payments, direct deposits, and refunds are negative."""

    iso_currency_code: str
    """The ISO-4217 currency code of the transaction."""

    enhancements: Enhancements
    """A grouping of the Plaid produced transaction enhancement fields."""


class ClientProvidedEnhancedTransactionDict(TypedDict):
    id: str
    description: str
    amount: float
    iso_currency_code: str
    enhancements: EnhancementsDict
