from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WarningCode(str, Enum):
    """The warning code identifies a specific kind of warning. ``OWNERS_UNAVAILABLE`` indicates that account-owner
    information is not available. ``INVESTMENTS_UNAVAILABLE`` indicates that Investments specific information is not
    available. ``TRANSACTIONS_UNAVAILABLE`` indicates that transactions information associated with Credit and
    Depository accounts are unavailable. The ``BANK_INCOME_INSIGHTS_*`` codes apply to the Bank Income add-on:
    ``BANK_INCOME_INSIGHTS_INSUFFICIENT_DATA`` indicates there was not enough data to compute Bank Income Insights;
    ``BANK_INCOME_INSIGHTS_INCOMPLETE`` indicates the Bank Income Insights flow was not completed;
    ``BANK_INCOME_INSIGHTS_STATUS_IN_PROGRESS`` indicates Bank Income Insights are still being computed;
    ``BANK_INCOME_INSIGHTS_INTERNAL_ERROR`` indicates an internal error occurred while computing Bank Income Insights;
    ``BANK_INCOME_INSIGHTS_MISMATCHED_DAYS_REQUESTED`` indicates the days requested for Bank Income Insights did not
    match that of the Asset Report."""

    OWNERS_UNAVAILABLE = "OWNERS_UNAVAILABLE"
    INVESTMENTS_UNAVAILABLE = "INVESTMENTS_UNAVAILABLE"
    TRANSACTIONS_UNAVAILABLE = "TRANSACTIONS_UNAVAILABLE"
    BANK_INCOME_INSIGHTS_INSUFFICIENT_DATA = "BANK_INCOME_INSIGHTS_INSUFFICIENT_DATA"
    BANK_INCOME_INSIGHTS_INCOMPLETE = "BANK_INCOME_INSIGHTS_INCOMPLETE"
    BANK_INCOME_INSIGHTS_STATUS_IN_PROGRESS = "BANK_INCOME_INSIGHTS_STATUS_IN_PROGRESS"
    BANK_INCOME_INSIGHTS_INTERNAL_ERROR = "BANK_INCOME_INSIGHTS_INTERNAL_ERROR"
    BANK_INCOME_INSIGHTS_MISMATCHED_DAYS_REQUESTED = "BANK_INCOME_INSIGHTS_MISMATCHED_DAYS_REQUESTED"

    __str__ = str.__str__


WarningCodeOrStr: TypeAlias = Annotated[WarningCode | str, open_enum_validator(WarningCode)]
