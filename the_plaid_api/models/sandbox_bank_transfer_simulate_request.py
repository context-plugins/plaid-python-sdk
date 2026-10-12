from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .bank_transfer_failure import BankTransferFailure, BankTransferFailureDict


class SandboxBankTransferSimulateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/bank_transfer/simulate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    bank_transfer_id: str
    """Plaid's unique identifier for a bank transfer."""

    event_type: str
    """The asynchronous event to be simulated. May be: ``posted``, ``failed``, or ``reversed``.

    An error will be returned if the event type is incompatible with the current transfer status. Compatible status -->
    event type transitions include:

    ``pending`` --> ``failed``

    ``pending`` --> ``posted``

    ``posted`` --> ``reversed``"""

    failure_reason: OptionalNullable[BankTransferFailure] = UNSET
    """The failure reason if the type of this transfer is ``"failed"`` or ``"reversed"``. Null value otherwise."""


class SandboxBankTransferSimulateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    bank_transfer_id: str
    event_type: str
    failure_reason: NotRequired[BankTransferFailureDict | None]
