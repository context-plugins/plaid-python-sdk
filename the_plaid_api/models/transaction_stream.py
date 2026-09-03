from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.recurring_transaction_frequency import RecurringTransactionFrequencyOrStr
from .enums.transaction_stream_status import TransactionStreamStatusOrStr
from .personal_finance_category import PersonalFinanceCategory, PersonalFinanceCategoryDict
from .transaction_stream_amount import TransactionStreamAmount, TransactionStreamAmountDict


class TransactionStream(SdkBaseModel):
    """A grouping of related transactions"""

    account_id: str
    """The ID of the account to which the stream belongs"""

    stream_id: str
    """A unique id for the stream"""

    category: list[str | None]
    """A hierarchical array of the categories to which this transaction belongs. See `Categories
    <https://plaid.com/docs/api/products/transactions/#categoriesget>`__.

    All implementations are encouraged to use the new ``personal_finance_category`` instead of ``category``.
    ``personal_finance_category`` provides more meaningful categorization and greater accuracy."""

    category_id: str | None
    """The ID of the category to which this transaction belongs. See `Categories
    <https://plaid.com/docs/api/products/transactions/#categoriesget>`__.

    All implementations are encouraged to use the new ``personal_finance_category`` instead of ``category``.
    ``personal_finance_category`` provides more meaningful categorization and greater accuracy."""

    description: str
    """A description of the transaction stream."""

    merchant_name: str | None
    """The merchant associated with the transaction stream."""

    first_date: Date
    """The posted date of the earliest transaction in the stream."""

    last_date: Date
    """The posted date of the latest transaction in the stream."""

    predicted_next_date: OptionalNullable[Date] = UNSET
    """The predicted date of the next payment. This will only be set if the next payment date can be predicted."""

    frequency: RecurringTransactionFrequencyOrStr
    """Describes the frequency of the transaction stream.

    ``WEEKLY``: Assigned to a transaction stream that occurs approximately every week.

    ``BIWEEKLY``: Assigned to a transaction stream that occurs approximately every 2 weeks.

    ``SEMI_MONTHLY``: Assigned to a transaction stream that occurs approximately twice per month. This frequency is
    typically seen for inflow transaction streams.

    ``MONTHLY``: Assigned to a transaction stream that occurs approximately every month.

    ``ANNUALLY``: Assigned to a transaction stream that occurs approximately every year.

    ``UNKNOWN``: Assigned to a transaction stream that does not fit any of the pre-defined frequencies."""

    transaction_ids: list[str]
    """An array of Plaid transaction IDs belonging to the stream, sorted by posted date."""

    average_amount: TransactionStreamAmount
    """Object with data pertaining to an amount on the transaction stream."""

    last_amount: TransactionStreamAmount
    """Object with data pertaining to an amount on the transaction stream."""

    is_active: bool
    """Indicates whether the transaction stream is still live."""

    status: TransactionStreamStatusOrStr
    """The current status of the transaction stream.

    ``MATURE``: A ``MATURE`` recurring stream should have at least 3 transactions and happen on a regular cadence (For
    Annual recurring stream, we will mark it ``MATURE`` after 2 instances).

    ``EARLY_DETECTION``: When a recurring transaction first appears in the transaction history and before it fulfills
    the requirement of a mature stream, the status will be ``EARLY_DETECTION``.

    ``TOMBSTONED``: A stream that was previously in the ``EARLY_DETECTION`` status will move to the ``TOMBSTONED``
    status when no further transactions were found at the next expected date.

    ``UNKNOWN``: A stream is assigned an ``UNKNOWN`` status when none of the other statuses are applicable."""

    personal_finance_category: OptionalNullable[PersonalFinanceCategory] = UNSET
    """Information describing the intent of the transaction. Most relevant for personal finance use cases, but not
    limited to such use cases.

    See the `taxonomy CSV file <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance
    categories. If you are migrating to personal finance categories from the legacy categories, also refer to the
    `migration guide <https://plaid.com/docs/transactions/pfc-migration/>`__."""

    is_user_modified: bool
    """As the ability to modify transactions streams has been discontinued, this field will always be ``false``."""

    last_user_modified_datetime: Optional[RFC3339DateTime] = UNSET
    """The date and time of the most recent user modification. This will only be set if ``is_user_modified`` is
    ``true``."""


class TransactionStreamDict(TypedDict):
    account_id: str
    stream_id: str
    category: list[str | None]
    category_id: str | None
    description: str
    merchant_name: str | None
    first_date: Date
    last_date: Date
    predicted_next_date: NotRequired[Date | None]
    frequency: RecurringTransactionFrequencyOrStr
    transaction_ids: list[str]
    average_amount: TransactionStreamAmount | TransactionStreamAmountDict
    last_amount: TransactionStreamAmount | TransactionStreamAmountDict
    is_active: bool
    status: TransactionStreamStatusOrStr
    personal_finance_category: NotRequired[PersonalFinanceCategory | PersonalFinanceCategoryDict | None]
    is_user_modified: bool
    last_user_modified_datetime: NotRequired[RFC3339DateTime]
