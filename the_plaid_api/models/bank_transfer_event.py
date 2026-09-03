from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .bank_transfer_failure import BankTransferFailure, BankTransferFailureDict
from .enums.bank_transfer_direction import BankTransferDirectionOrStr
from .enums.bank_transfer_event_type import BankTransferEventTypeOrStr
from .enums.bank_transfer_type import BankTransferTypeOrStr
from .receiver_details import ReceiverDetails, ReceiverDetailsDict


class BankTransferEvent(SdkBaseModel):
    """Represents an event in the Bank Transfers API."""

    event_id: int
    """Plaid's unique identifier for this event. IDs are sequential unsigned 64-bit integers."""

    timestamp: RFC3339DateTime
    """The datetime when this event occurred. This will be of the form ``2006-01-02T15:04:05Z``."""

    event_type: BankTransferEventTypeOrStr
    """The type of event that this bank transfer represents.

    ``pending``: A new transfer was created; it is in the pending state.

    ``cancelled``: The transfer was cancelled by the client.

    ``failed``: The transfer failed, no funds were moved.

    ``posted``: The transfer has been successfully submitted to the payment network.

    ``reversed``: A posted transfer was reversed."""

    account_id: str
    """The account ID associated with the bank transfer."""

    bank_transfer_id: str
    """Plaid's unique identifier for a bank transfer."""

    origination_account_id: str | None
    """The ID of the origination account that this balance belongs to."""

    bank_transfer_type: BankTransferTypeOrStr
    """The type of bank transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money
    into the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    bank_transfer_amount: str
    """The bank transfer amount."""

    bank_transfer_iso_currency_code: str
    """The currency of the bank transfer amount."""

    failure_reason: BankTransferFailure | None
    """The failure reason if the type of this transfer is ``"failed"`` or ``"reversed"``. Null value otherwise."""

    direction: BankTransferDirectionOrStr | None
    """Indicates the direction of the transfer: ``outbound`` for API-initiated transfers, or ``inbound`` for payments
    received by the FBO account."""

    receiver_details: ReceiverDetails | None
    """Additional details for receiver events. Currently always ``null``."""


class BankTransferEventDict(TypedDict):
    event_id: int
    timestamp: RFC3339DateTime
    event_type: BankTransferEventTypeOrStr
    account_id: str
    bank_transfer_id: str
    origination_account_id: str | None
    bank_transfer_type: BankTransferTypeOrStr
    bank_transfer_amount: str
    bank_transfer_iso_currency_code: str
    failure_reason: BankTransferFailure | BankTransferFailureDict | None
    direction: BankTransferDirectionOrStr | None
    receiver_details: ReceiverDetails | ReceiverDetailsDict | None
