from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class TransactionData(SdkBaseModel):
    """Information about the matched direct deposit transaction used to verify a user's payroll information."""

    description: str
    """The description of the transaction."""

    amount: float
    """The amount of the transaction."""

    date: Date
    """The date of the transaction, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format ("yyyy-mm-dd")."""

    account_id: str
    """A unique identifier for the end user's account."""

    transaction_id: str
    """A unique identifier for the transaction."""


class TransactionDataDict(TypedDict):
    description: str
    amount: float
    date: Date
    account_id: str
    transaction_id: str
