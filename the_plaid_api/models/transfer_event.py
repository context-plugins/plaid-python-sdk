from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.omittable_transfer_type import OmittableTransferTypeOrStr
from .enums.transfer_event_type import TransferEventTypeOrStr
from .transfer_failure import TransferFailure, TransferFailureDict


class TransferEvent(SdkBaseModel):
    """Represents an event in the Transfers API."""

    event_id: int
    """Plaid's unique identifier for this event. IDs are sequential unsigned 64-bit integers."""

    timestamp: RFC3339DateTime
    """The datetime when this event occurred. This will be of the form ``2006-01-02T15:04:05Z``."""

    event_type: TransferEventTypeOrStr
    """The type of event that this transfer represents. Event types with prefix ``sweep`` represent events for Plaid
    Ledger sweeps.

    ``pending``: A new transfer was created; it is in the pending state.

    ``cancelled``: The transfer was cancelled by the client.

    ``failed``: The transfer failed, no funds were moved.

    ``posted``: The transfer has been successfully submitted to the payment network.

    ``settled``: The transfer has been successfully completed by the payment network.

    ``funds_available``: Funds from the transfer have been released from hold and applied to the ledger's available
    balance. (Only applicable to ACH debits.)

    ``guaranteed``: The transfer has been fully guaranteed by Plaid.

    ``returned``: A posted transfer was returned.

    ``guarantee_reimbursed``: Plaid reimbursed the client for the loss on a returned guaranteed transfer. The
    ``event_amount`` is the reimbursed amount.

    ``client_return_recovered``: The client reported recovering the loss on a returned transfer via
    ``/transfer/return/recover``, and Plaid debited the recovered amount from the client's ledger. The ``event_amount``
    is the recovered amount.

    ``plaid_return_recovered``: Plaid recovered the loss on a returned transfer by successfully reinitiating it. The
    ``event_amount`` is the recovered amount. Client should stop their return recovery effort.

    ``swept``: The transfer was swept to / from the sweep account.

    ``swept_settled``: Credits are available to be withdrawn or debits have been deducted from the customer's business
    checking account.

    ``return_swept``: Due to the transfer being returned, funds were pulled from or pushed back to the sweep account.

    ``sweep.pending``: A new ledger sweep was created; it is in the pending state.

    ``sweep.posted``: The ledger sweep has been successfully submitted to the payment network.

    ``sweep.settled``: The transaction has settled in the funding account. This means that funds withdrawn from Plaid
    Ledger balance have reached the funding account, or funds to be deposited into the Plaid Ledger Balance have been
    pulled, and the hold period has begun.

    ``sweep.returned``: A posted ledger sweep was returned.

    ``sweep.failed``: The ledger sweep failed, no funds were moved.

    ``sweep.funds_available``: Funds from the ledger sweep have been released from hold and applied to the ledger's
    available balance. This is only applicable to debits.

    ``refund.pending``: A new refund was created; it is in the pending state.

    ``refund.cancelled``: The refund was cancelled.

    ``refund.failed``: The refund failed, no funds were moved.

    ``refund.posted``: The refund has been successfully submitted to the payment network.

    ``refund.settled``: The refund transaction has settled in the Plaid linked account.

    ``refund.returned``: A posted refund was returned.

    ``refund.swept``: The refund was swept from the sweep account.

    ``refund.return_swept``: Due to the refund being returned, funds were pushed back to the sweep account."""

    account_id: Optional[str] = UNSET
    """The account ID associated with the transfer. This field is omitted for Plaid Ledger Sweep events."""

    funding_account_id: str | None
    """The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of
    your business checking accounts will be credited or debited."""

    ledger_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a Plaid Ledger Balance."""

    transfer_id: str
    """Plaid's unique identifier for a transfer. This field is an empty string for Plaid Ledger Sweep events."""

    origination_account_id: str | None
    """The ID of the origination account that this balance belongs to."""

    transfer_type: Optional[OmittableTransferTypeOrStr] = UNSET
    """The type of transfer. Valid values are ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account. This field is
    omitted for Plaid Ledger Sweep events."""

    transfer_amount: Optional[str] = UNSET
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). This field is omitted for
    Plaid Ledger Sweep events."""

    failure_reason: TransferFailure | None
    """The failure reason if the event type for a transfer is ``"failed"`` or ``"returned"``. Null value otherwise."""

    sweep_id: str | None
    """Plaid's unique identifier for a sweep."""

    sweep_amount: str | None
    """A signed amount of how much was ``swept`` or ``return_swept`` for this transfer (decimal string with two digits
    of precision e.g. "-5.50")."""

    event_amount: OptionalNullable[str] = UNSET
    """A signed amount associated with this event (decimal string with two digits of precision e.g. "10.00" or
    "-10.00")."""

    refund_id: str | None
    """Plaid's unique identifier for a refund. A non-null value indicates the event is for the associated refund of the
    transfer."""

    originator_client_id: str | None
    """The Plaid client ID that is the originator of the transfer that this event applies to. Only present if the
    transfer was created on behalf of another client as a third-party sender (TPS)."""

    intent_id: OptionalNullable[str] = UNSET
    """The ``id`` returned by the ``/transfer/intent/create`` endpoint, for transfers created via Transfer UI. For
    transfers not created by Transfer UI, the value is ``null``. This will currently only be populated for RfP
    transfers."""

    wire_return_fee: OptionalNullable[str] = UNSET
    """The fee amount deducted from the original transfer during a wire return, if applicable."""


class TransferEventDict(TypedDict):
    event_id: int
    timestamp: RFC3339DateTime
    event_type: TransferEventTypeOrStr
    account_id: NotRequired[str]
    funding_account_id: str | None
    ledger_id: NotRequired[str | None]
    transfer_id: str
    origination_account_id: str | None
    transfer_type: NotRequired[OmittableTransferTypeOrStr]
    transfer_amount: NotRequired[str]
    failure_reason: TransferFailure | TransferFailureDict | None
    sweep_id: str | None
    sweep_amount: str | None
    event_amount: NotRequired[str | None]
    refund_id: str | None
    originator_client_id: str | None
    intent_id: NotRequired[str | None]
    wire_return_fee: NotRequired[str | None]
