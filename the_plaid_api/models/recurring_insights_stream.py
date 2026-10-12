from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.recurring_transaction_frequency import RecurringTransactionFrequencyOrStr
from .enums.transaction_stream_status import TransactionStreamStatusOrStr
from .transaction_stream_amount import TransactionStreamAmount, TransactionStreamAmountDict


class RecurringInsightsStream(SdkBaseModel):
    """Insights object for recurring transactions streams."""

    stream_id: str
    """A unique id for the stream."""

    description: Optional[str] = UNSET
    """The client-provided raw description of the most recent transaction in the stream."""

    merchant_name: str
    """The merchant or primary counterparty associated with the transaction stream."""

    oldest_transaction_date: Optional[Date] = UNSET
    """The posted date of the earliest transaction in the stream."""

    newest_transaction_date: Optional[Date] = UNSET
    """The posted date of the latest transaction in the stream."""

    average_days_apart: float
    """The average number of days between each of the recurring transactions."""

    frequency: Optional[RecurringTransactionFrequencyOrStr] = UNSET
    """Describes the frequency of the transaction stream.

    ``WEEKLY``: Assigned to a transaction stream that occurs approximately every week.

    ``BIWEEKLY``: Assigned to a transaction stream that occurs approximately every 2 weeks.

    ``SEMI_MONTHLY``: Assigned to a transaction stream that occurs approximately twice per month. This frequency is
    typically seen for inflow transaction streams.

    ``MONTHLY``: Assigned to a transaction stream that occurs approximately every month.

    ``ANNUALLY``: Assigned to a transaction stream that occurs approximately every year.

    ``UNKNOWN``: Assigned to a transaction stream that does not fit any of the pre-defined frequencies."""

    transaction_count: Optional[int] = UNSET
    """The number of transactions in this stream."""

    transaction_ids: Optional[list[str]] = UNSET
    """An array of Plaid transaction IDs belonging to the stream, sorted by posted date."""

    average_amount: Optional[TransactionStreamAmount] = UNSET
    """Object with data pertaining to an amount on the transaction stream."""

    newest_transaction_amount: Optional[TransactionStreamAmount] = UNSET
    """Object with data pertaining to an amount on the transaction stream."""

    is_active: bool
    """Indicates whether the transaction stream is still live."""

    status: Optional[TransactionStreamStatusOrStr] = UNSET
    """The current status of the transaction stream.

    ``MATURE``: A ``MATURE`` recurring stream should have at least 3 transactions and happen on a regular cadence (For
    Annual recurring stream, we will mark it ``MATURE`` after 2 instances).

    ``EARLY_DETECTION``: When a recurring transaction first appears in the transaction history and before it fulfills
    the requirement of a mature stream, the status will be ``EARLY_DETECTION``.

    ``TOMBSTONED``: A stream that was previously in the ``EARLY_DETECTION`` status will move to the ``TOMBSTONED``
    status when no further transactions were found at the next expected date.

    ``UNKNOWN``: A stream is assigned an ``UNKNOWN`` status when none of the other statuses are applicable."""

    personal_finance_category_primary: Optional[str] = UNSET
    """The primary category associated with the transaction stream."""

    personal_finance_category_detailed: Optional[str] = UNSET
    """The detailed category associated with the transaction stream."""


class RecurringInsightsStreamDict(TypedDict):
    stream_id: str
    description: NotRequired[str]
    merchant_name: str
    oldest_transaction_date: NotRequired[Date]
    newest_transaction_date: NotRequired[Date]
    average_days_apart: float
    frequency: NotRequired[RecurringTransactionFrequencyOrStr]
    transaction_count: NotRequired[int]
    transaction_ids: NotRequired[list[str]]
    average_amount: NotRequired[TransactionStreamAmountDict]
    newest_transaction_amount: NotRequired[TransactionStreamAmountDict]
    is_active: bool
    status: NotRequired[TransactionStreamStatusOrStr]
    personal_finance_category_primary: NotRequired[str]
    personal_finance_category_detailed: NotRequired[str]
