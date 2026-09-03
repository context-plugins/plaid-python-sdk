from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_sweep import TransferSweep, TransferSweepDict


class TransferLedgerWithdrawResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/ledger/withdraw``"""

    sweep: TransferSweep
    """Describes a sweep of funds to / from the sweep account.

    A sweep is associated with many sweep events (events of type ``swept`` or ``return_swept``) which can be retrieved
    by invoking the ``/transfer/event/list`` endpoint with the corresponding ``sweep_id``.

    ``swept`` events occur when the transfer amount is credited or debited from your sweep account, depending on the
    ``type`` of the transfer. ``return_swept`` events occur when a transfer is returned and Plaid undoes the credit or
    debit.

    The total sum of the ``swept`` and ``return_swept`` events is equal to the ``amount`` of the sweep Plaid creates and
    matches the amount of the entry on your sweep account ledger."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferLedgerWithdrawResponseDict(TypedDict):
    sweep: TransferSweep | TransferSweepDict
    request_id: str
