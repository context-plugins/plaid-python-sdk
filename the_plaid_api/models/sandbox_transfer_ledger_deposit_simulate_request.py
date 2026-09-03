from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.transfer_ledger_sweep_simulate_event_type import TransferLedgerSweepSimulateEventTypeOrStr
from .transfer_failure import TransferFailure, TransferFailureDict


class SandboxTransferLedgerDepositSimulateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/ledger/deposit/simulate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    sweep_id: str
    """Plaid's unique identifier for a sweep."""

    event_type: TransferLedgerSweepSimulateEventTypeOrStr
    """The asynchronous event to be simulated. May be: ``posted``, ``settled``, ``failed``, or ``returned``.

    An error will be returned if the event type is incompatible with the current ledger sweep status. Compatible status
    --> event type transitions include:

    ``sweep.pending`` --> ``sweep.posted``

    ``sweep.pending`` --> ``sweep.failed``

    ``sweep.posted`` --> ``sweep.settled``

    ``sweep.posted`` --> ``sweep.returned``

    ``sweep.settled`` --> ``sweep.returned``"""

    failure_reason: OptionalNullable[TransferFailure] = UNSET
    """The failure reason if the event type for a transfer is ``"failed"`` or ``"returned"``. Null value otherwise."""


class SandboxTransferLedgerDepositSimulateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    sweep_id: str
    event_type: TransferLedgerSweepSimulateEventTypeOrStr
    failure_reason: NotRequired[TransferFailure | TransferFailureDict | None]
