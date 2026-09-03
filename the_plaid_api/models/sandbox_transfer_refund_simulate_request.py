from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .transfer_failure import TransferFailure, TransferFailureDict


class SandboxTransferRefundSimulateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/refund/simulate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    refund_id: str
    """Plaid's unique identifier for a refund."""

    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock. If provided, the event to be simulated is created at the
    ``virtual_time`` on the provided ``test_clock``."""

    event_type: str
    """The asynchronous event to be simulated. May be: ``refund.posted``, ``refund.settled``, ``refund.failed``, or
    ``refund.returned``.

    An error will be returned if the event type is incompatible with the current refund status. Compatible status -->
    event type transitions include:

    ``refund.pending`` --> ``refund.failed``

    ``refund.pending`` --> ``refund.posted``

    ``refund.posted`` --> ``refund.returned``

    ``refund.posted`` --> ``refund.settled``

    ``refund.posted`` events can only be simulated if the refunded transfer has been transitioned to settled. This
    mimics the ordering of events in Production."""

    failure_reason: OptionalNullable[TransferFailure] = UNSET
    """The failure reason if the event type for a transfer is ``"failed"`` or ``"returned"``. Null value otherwise."""

    webhook: Optional[str] = UNSET
    """The webhook URL to which a ``TRANSFER_EVENTS_UPDATE`` webhook should be sent."""


class SandboxTransferRefundSimulateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    refund_id: str
    test_clock_id: NotRequired[str | None]
    event_type: str
    failure_reason: NotRequired[TransferFailure | TransferFailureDict | None]
    webhook: NotRequired[str]
