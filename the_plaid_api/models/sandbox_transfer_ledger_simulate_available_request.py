from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SandboxTransferLedgerSimulateAvailableRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/ledger/simulate_available``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    ledger_id: OptionalNullable[str] = UNSET
    """Specify which ledger balance to simulate converting pending balance to available balance. If this field is left
    blank, this will default to the id of the default ledger balance."""

    originator_client_id: OptionalNullable[str] = UNSET
    """Client ID of the end customer (i.e. the originator). Only applicable to Transfer for Platforms customers."""

    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock. If provided, only the pending balance that is due before the
    ``virtual_time`` on the test clock will be converted."""

    webhook: Optional[str] = UNSET
    """The webhook URL to which a ``TRANSFER_EVENTS_UPDATE`` webhook should be sent."""


class SandboxTransferLedgerSimulateAvailableRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    ledger_id: NotRequired[str | None]
    originator_client_id: NotRequired[str | None]
    test_clock_id: NotRequired[str | None]
    webhook: NotRequired[str]
