from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SandboxTransferSweepSimulateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/sweep/simulate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock. If provided, the sweep to be simulated is created on the day of the
    ``virtual_time`` on the ``test_clock``. If the date of ``virtual_time`` is on weekend or a federal holiday, the next
    available banking day is used."""

    webhook: Optional[str] = UNSET
    """The webhook URL to which a ``TRANSFER_EVENTS_UPDATE`` webhook should be sent."""


class SandboxTransferSweepSimulateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    test_clock_id: NotRequired[str | None]
    webhook: NotRequired[str]
