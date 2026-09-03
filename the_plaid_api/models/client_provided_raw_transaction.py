from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClientProvidedRawTransaction(SdkBaseModel):
    """A client-provided transaction for Plaid to enhance."""

    id: str
    """A unique ID for the transaction used to help you tie data back to your systems."""

    description: str
    """The raw description of the transaction."""

    amount: float
    """The value of the transaction with direction. (NOTE: this will affect enrichment results, so directions are
    important).
      Negative (-) for credits (e.g., incoming transfers, refunds)
      Positive (+) for debits (e.g., purchases, fees, outgoing transfers)"""

    iso_currency_code: str
    """The ISO-4217 currency code of the transaction e.g. USD."""


class ClientProvidedRawTransactionDict(TypedDict):
    id: str
    description: str
    amount: float
    iso_currency_code: str
