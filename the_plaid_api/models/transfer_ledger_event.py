from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TransferLedgerEvent(SdkBaseModel):
    """Represents a ledger event in the Transfers API."""

    ledger_event_id: str
    """Plaid's unique identifier for this ledger event."""

    ledger_id: str
    """The ID of the ledger this event belongs to."""

    amount: str
    """The amount of the ledger event as a decimal string."""

    transfer_id: OptionalNullable[str] = UNSET
    """The ID of the transfer source that triggered this ledger event."""

    refund_id: OptionalNullable[str] = UNSET
    """The ID of the refund source that triggered this ledger event."""

    sweep_id: OptionalNullable[str] = UNSET
    """The ID of the sweep source that triggered this ledger event."""

    description: str
    """A description of the ledger event."""

    pending_balance: str
    """The new pending balance after this event."""

    available_balance: str
    """The new available balance after this event."""

    type_: str = Field(alias="type")
    """The type of balance that was impacted by this event."""

    timestamp: RFC3339DateTime
    """The datetime when this ledger event occurred."""


class TransferLedgerEventDict(TypedDict):
    ledger_event_id: str
    ledger_id: str
    amount: str
    transfer_id: NotRequired[str | None]
    refund_id: NotRequired[str | None]
    sweep_id: NotRequired[str | None]
    description: str
    pending_balance: str
    available_balance: str
    type_: str
    timestamp: RFC3339DateTime
