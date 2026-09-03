from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecurringTransactionFrequency(str, Enum):
    """Describes the frequency of the transaction stream.

    ``WEEKLY``: Assigned to a transaction stream that occurs approximately every week.

    ``BIWEEKLY``: Assigned to a transaction stream that occurs approximately every 2 weeks.

    ``SEMI_MONTHLY``: Assigned to a transaction stream that occurs approximately twice per month. This frequency is
    typically seen for inflow transaction streams.

    ``MONTHLY``: Assigned to a transaction stream that occurs approximately every month.

    ``ANNUALLY``: Assigned to a transaction stream that occurs approximately every year.

    ``UNKNOWN``: Assigned to a transaction stream that does not fit any of the pre-defined frequencies."""

    UNKNOWN = "UNKNOWN"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"
    ANNUALLY = "ANNUALLY"

    __str__ = str.__str__


RecurringTransactionFrequencyOrStr: TypeAlias = Annotated[
    RecurringTransactionFrequency | str, open_enum_validator(RecurringTransactionFrequency)
]
