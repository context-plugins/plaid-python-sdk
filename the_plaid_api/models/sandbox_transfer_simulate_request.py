from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .transfer_failure import TransferFailure, TransferFailureDict


class SandboxTransferSimulateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/simulate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    transfer_id: str
    """Plaid's unique identifier for a transfer."""

    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock. If provided, the event to be simulated is created at the
    ``virtual_time`` on the provided ``test_clock``."""

    event_type: str
    """The asynchronous event to be simulated. May be: ``posted``, ``settled``, ``failed``, ``funds_available``, or
    ``returned``.

    An error will be returned if the event type is incompatible with the current transfer status. Compatible status -->
    event type transitions include:

    ``pending`` --> ``failed``

    ``pending`` --> ``posted``

    ``posted`` --> ``returned``

    ``posted`` --> ``settled``

    ``settled`` --> ``funds_available`` (only applicable to ACH debits.)"""

    failure_reason: OptionalNullable[TransferFailure] = UNSET
    """The failure reason if the event type for a transfer is ``"failed"`` or ``"returned"``. Null value otherwise."""

    webhook: Optional[str] = UNSET
    """The webhook URL to which a ``TRANSFER_EVENTS_UPDATE`` webhook should be sent."""


class SandboxTransferSimulateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    transfer_id: str
    test_clock_id: NotRequired[str | None]
    event_type: str
    failure_reason: NotRequired[TransferFailure | TransferFailureDict | None]
    webhook: NotRequired[str]
