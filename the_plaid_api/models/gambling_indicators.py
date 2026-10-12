from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .monthly_average import MonthlyAverage, MonthlyAverageDict
from .monthly_summary import MonthlySummary, MonthlySummaryDict


class GamblingIndicators(SdkBaseModel):
    """Insights into gambling-related transactions, including frequency, amounts, and top merchants."""

    amount: OptionalNullable[float] = UNSET
    """The total value of transactions that fall into the ``GAMBLING`` credit category, across all the accounts in the
    report."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the amount. Always ``null`` if ``unofficial_currency_code`` is non-``null``."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the amount. Always ``null`` if ``iso_currency_code`` is
    non-``null``.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    monthly_average: OptionalNullable[MonthlyAverage] = UNSET
    """The monthly average amount calculated by dividing the total by the number of calendar months in the time
    period."""

    top_merchants: Optional[list[str]] = UNSET
    """Up to 3 top merchants that the user had the most transactions for in the given time window, in descending order
    of total spend.

    If the user has not spent money on any merchants in the given time window, this list will be empty."""

    transactions_count: OptionalNullable[int] = UNSET
    """The total number of transactions that fall into the ``GAMBLING`` credit category, across all the accounts in the
    report."""

    monthly_summaries: Optional[list[MonthlySummary | None]] = UNSET
    """The monthly summaries of the transactions that fall into the ``GAMBLING`` category within the given time window,
    across all the accounts in the report."""

    days_since_last_occurrence: OptionalNullable[int] = UNSET
    """The number of days since the last transaction that falls into the ``GAMBLING`` category, across all the accounts
    in the report."""

    percentage_of_income: OptionalNullable[float] = UNSET
    """The percentage of the user's monthly inflows that was spent on transactions that fall into the ``GAMBLING``
    category within the given time window, across all the accounts in the report. For example, a value of 100 indicates
    that 100% of the inflows were spent on transactions that fall into the ``GAMBLING`` credit category. If there's no
    available income for the given time period, this field value will be ``-1``"""


class GamblingIndicatorsDict(TypedDict):
    amount: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    monthly_average: NotRequired[MonthlyAverageDict | None]
    top_merchants: NotRequired[list[str]]
    transactions_count: NotRequired[int | None]
    monthly_summaries: NotRequired[list[MonthlySummaryDict | None]]
    days_since_last_occurrence: NotRequired[int | None]
    percentage_of_income: NotRequired[float | None]
