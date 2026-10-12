from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_ledger_balance import TransferLedgerBalance, TransferLedgerBalanceDict


class TransferLedgerGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/ledger/get``"""

    ledger_id: str
    """The unique identifier of the Ledger that was returned."""

    balance: TransferLedgerBalance
    """Information about the balance of the ledger held with Plaid."""

    name: str
    """The name of the Ledger"""

    is_default: bool
    """Whether this Ledger is the client's default ledger."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferLedgerGetResponseDict(TypedDict):
    ledger_id: str
    balance: TransferLedgerBalanceDict
    name: str
    is_default: bool
    request_id: str
