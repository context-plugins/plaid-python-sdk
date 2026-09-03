from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferLedgerBalance(SdkBaseModel):
    """Information about the balance of the ledger held with Plaid."""

    available: str
    """The amount of this balance available for use (decimal string with two digits of precision e.g. "10.00")."""

    pending: str
    """The amount of pending funds that are in processing (decimal string with two digits of precision e.g. "10.00")."""


class TransferLedgerBalanceDict(TypedDict):
    available: str
    pending: str
