from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.sweep_status import SweepStatusOrStr
from .enums.sweep_trigger import SweepTriggerOrStr


class TransferSweepListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/sweep/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The start ``created`` datetime of sweeps to return (RFC 3339 format)."""

    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The end ``created`` datetime of sweeps to return (RFC 3339 format)."""

    count: int | None = 25
    """The maximum number of sweeps to return."""

    offset: int = 0
    """The number of sweeps to skip before returning results."""

    amount: OptionalNullable[str] = UNSET
    """Filter sweeps to only those with the specified amount."""

    status: OptionalNullable[SweepStatusOrStr] = UNSET
    """The status of a sweep transfer

    ``"pending"`` - The sweep is currently pending ``"posted"`` - The sweep has been posted ``"settled"`` - The sweep
    has settled. This is the terminal state of a successful credit sweep. ``"returned"`` - The sweep has been returned.
    This is the terminal state of a returned sweep. Returns of a sweep are extremely rare, since sweeps are money
    movement between your own bank account and your own Ledger. ``"funds_available"`` - Funds from the sweep have been
    released from hold and applied to the ledger's available balance. (Only applicable to deposits.) This is the
    terminal state of a successful deposit sweep. ``"failed"`` - The sweep has failed. This is the terminal state of a
    failed sweep."""

    originator_client_id: OptionalNullable[str] = UNSET
    """Filter sweeps to only those with the specified originator client."""

    funding_account_id: OptionalNullable[str] = UNSET
    """Filter sweeps to only those with the specified ``funding_account_id``."""

    transfer_id: OptionalNullable[str] = UNSET
    """Filter sweeps to only those with the included ``transfer_id``."""

    trigger: OptionalNullable[SweepTriggerOrStr] = UNSET
    """The trigger of the sweep

    ``"manual"`` - The sweep is created manually by the customer ``"incoming"`` - The sweep is created by incoming funds
    flow (e.g. Incoming Wire) ``"balance_threshold"`` - The sweep is created by balance threshold setting
    ``"automatic_aggregate"`` - The sweep is created by the Plaid automatic aggregation process. These funds did not
    pass through the Plaid Ledger balance."""


class TransferSweepListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_date: NotRequired[RFC3339DateTime | None]
    end_date: NotRequired[RFC3339DateTime | None]
    count: NotRequired[int | None]
    offset: NotRequired[int]
    amount: NotRequired[str | None]
    status: NotRequired[SweepStatusOrStr | None]
    originator_client_id: NotRequired[str | None]
    funding_account_id: NotRequired[str | None]
    transfer_id: NotRequired[str | None]
    trigger: NotRequired[SweepTriggerOrStr | None]
