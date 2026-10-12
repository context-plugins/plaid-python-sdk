from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.transfer_refund_status import TransferRefundStatusOrStr
from .transfer_refund_failure import TransferRefundFailure, TransferRefundFailureDict


class TransferRefund(SdkBaseModel):
    """Represents a refund within the Transfers API."""

    id: str
    """Plaid's unique identifier for a refund."""

    transfer_id: str
    """The ID of the transfer to refund."""

    amount: str
    """The amount of the refund (decimal string with two digits of precision e.g. "10.00")."""

    status: TransferRefundStatusOrStr
    """The status of the refund.

    ``pending``: A new refund was created; it is in the pending state. ``posted``: The refund has been successfully
    submitted to the payment network. ``settled``: Credits have been refunded to the Plaid linked account.
    ``cancelled``: The refund was cancelled by the client. ``failed``: The refund has failed. ``returned``: The refund
    was returned."""

    failure_reason: TransferRefundFailure | None
    """The failure reason if the status for a refund is ``"failed"`` or ``"returned"``. Null value otherwise."""

    ledger_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a Plaid Ledger Balance."""

    created: RFC3339DateTime
    """The datetime when this refund was created. This will be of the form ``2006-01-02T15:04:05Z``"""

    network_trace_id: OptionalNullable[str] = UNSET
    """The trace identifier for the transfer based on its network. This will only be set after the transfer has posted.

    For ``ach`` or ``same-day-ach`` transfers, this is the ACH trace number. For ``rtp`` transfers, this is the
    Transaction Identification number. For ``wire`` transfers, this is the IMAD (Input Message Accountability Data)
    number."""


class TransferRefundDict(TypedDict):
    id: str
    transfer_id: str
    amount: str
    status: TransferRefundStatusOrStr
    failure_reason: TransferRefundFailureDict | None
    ledger_id: NotRequired[str | None]
    created: RFC3339DateTime
    network_trace_id: NotRequired[str | None]
