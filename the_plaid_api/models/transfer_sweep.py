from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.sweep_status import SweepStatusOrStr
from .enums.sweep_trigger import SweepTriggerOrStr
from .sweep_failure import SweepFailure, SweepFailureDict


class TransferSweep(SdkBaseModel):
    """Describes a sweep of funds to / from the sweep account.

    A sweep is associated with many sweep events (events of type ``swept`` or ``return_swept``) which can be retrieved
    by invoking the ``/transfer/event/list`` endpoint with the corresponding ``sweep_id``.

    ``swept`` events occur when the transfer amount is credited or debited from your sweep account, depending on the
    ``type`` of the transfer. ``return_swept`` events occur when a transfer is returned and Plaid undoes the credit or
    debit.

    The total sum of the ``swept`` and ``return_swept`` events is equal to the ``amount`` of the sweep Plaid creates and
    matches the amount of the entry on your sweep account ledger."""

    id: str
    """Identifier of the sweep."""

    funding_account_id: str
    """The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business
    checking accounts will be credited or debited."""

    ledger_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a Plaid Ledger Balance."""

    created: RFC3339DateTime
    """The datetime when the sweep occurred, in RFC 3339 format."""

    amount: str
    """Signed decimal amount of the sweep as it appears on your sweep account ledger (e.g. "-10.00")

    If amount is not present, the sweep was net-settled to zero and outstanding debits and credits between the sweep
    account and Plaid are balanced."""

    iso_currency_code: str
    """The currency of the sweep, e.g. "USD"."""

    settled: Date | None
    """The date when the sweep settled, in the YYYY-MM-DD format."""

    expected_funds_available_date: OptionalNullable[Date] = UNSET
    """The expected date when funds from a ledger deposit will be made available and can be withdrawn from the
    associated ledger balance. Only applies to deposits. This will be of the form YYYY-MM-DD."""

    status: OptionalNullable[SweepStatusOrStr] = UNSET
    """The status of a sweep transfer

    ``"pending"`` - The sweep is currently pending ``"posted"`` - The sweep has been posted ``"settled"`` - The sweep
    has settled. This is the terminal state of a successful credit sweep. ``"returned"`` - The sweep has been returned.
    This is the terminal state of a returned sweep. Returns of a sweep are extremely rare, since sweeps are money
    movement between your own bank account and your own Ledger. ``"funds_available"`` - Funds from the sweep have been
    released from hold and applied to the ledger's available balance. (Only applicable to deposits.) This is the
    terminal state of a successful deposit sweep. ``"failed"`` - The sweep has failed. This is the terminal state of a
    failed sweep."""

    trigger: OptionalNullable[SweepTriggerOrStr] = UNSET
    """The trigger of the sweep

    ``"manual"`` - The sweep is created manually by the customer ``"incoming"`` - The sweep is created by incoming funds
    flow (e.g. Incoming Wire) ``"balance_threshold"`` - The sweep is created by balance threshold setting
    ``"automatic_aggregate"`` - The sweep is created by the Plaid automatic aggregation process. These funds did not
    pass through the Plaid Ledger balance."""

    description: Optional[str] = UNSET
    """The description of the deposit that will be passed to the receiving bank (up to 10 characters). Note that banks
    utilize this field differently, and may or may not show it on the bank statement."""

    network_trace_id: OptionalNullable[str] = UNSET
    """The trace identifier for the transfer based on its network. This will only be set after the transfer has posted.

    For ``ach`` or ``same-day-ach`` transfers, this is the ACH trace number. For ``rtp`` transfers, this is the
    Transaction Identification number. For ``wire`` transfers, this is the IMAD (Input Message Accountability Data)
    number."""

    failure_reason: OptionalNullable[SweepFailure] = UNSET
    """The failure reason if the status for a sweep is ``"failed"`` or ``"returned"``. Null value otherwise."""


class TransferSweepDict(TypedDict):
    id: str
    funding_account_id: str
    ledger_id: NotRequired[str | None]
    created: RFC3339DateTime
    amount: str
    iso_currency_code: str
    settled: Date | None
    expected_funds_available_date: NotRequired[Date | None]
    status: NotRequired[SweepStatusOrStr | None]
    trigger: NotRequired[SweepTriggerOrStr | None]
    description: NotRequired[str]
    network_trace_id: NotRequired[str | None]
    failure_reason: NotRequired[SweepFailure | SweepFailureDict | None]
