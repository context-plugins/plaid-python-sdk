from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .amount_with_currency import AmountWithCurrency, AmountWithCurrencyDict
from .negative_balance_occurrence import NegativeBalanceOccurrence, NegativeBalanceOccurrenceDict


class NegativeBalanceInsights(SdkBaseModel):
    """Insights into negative balance occurrences, including frequency, duration, and minimum balance details."""

    days_since_last_occurrence: OptionalNullable[int] = UNSET
    """The number of days since the last transaction that caused any account in the report to have a negative balance.

    This value is inclusive of the date of the last negative balance, meaning that if the last negative balance occurred
    today, this value will be ``0``."""

    days_with_negative_balance: OptionalNullable[int] = UNSET
    """The number of aggregated days that the accounts in the report has had a negative balance within the given time
    window."""

    minimum_balance: OptionalNullable[AmountWithCurrency] = UNSET
    """A monetary amount with its associated currency information, supporting both official and unofficial currency
    codes."""

    occurrences: Optional[list[NegativeBalanceOccurrence | None]] = UNSET
    """The summary of the negative balance occurrences for this account.

    If the user has not had a negative balance in the account in the given time window, this list will be empty."""


class NegativeBalanceInsightsDict(TypedDict):
    days_since_last_occurrence: NotRequired[int | None]
    days_with_negative_balance: NotRequired[int | None]
    minimum_balance: NotRequired[AmountWithCurrencyDict | None]
    occurrences: NotRequired[list[NegativeBalanceOccurrenceDict | None]]
