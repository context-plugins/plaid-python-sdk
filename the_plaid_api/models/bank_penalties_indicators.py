from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .category_expenses import CategoryExpenses, CategoryExpensesDict
from .monthly_average import MonthlyAverage, MonthlyAverageDict
from .monthly_summary import MonthlySummary, MonthlySummaryDict


class BankPenaltiesIndicators(SdkBaseModel):
    """Insights into bank penalties and fees, including overdraft fees, NSF fees, and other bank-imposed charges."""

    amount: OptionalNullable[float] = UNSET
    """The total value of outflow transactions categorized as ``BANK_PENALTIES``, across all the accounts in the report
    within the requested time window."""

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

    category_details: OptionalNullable[list[CategoryExpenses]] = UNSET
    """Detailed categories view of all the transactions that fall into the ``BANK_PENALTIES`` credit category within the
    given time window, across all the accounts in the report."""

    transactions_count: OptionalNullable[int] = UNSET
    """The total number of transactions that fall into the ``BANK_PENALTIES`` credit category, across all the accounts
    in the report."""

    monthly_summaries: OptionalNullable[list[MonthlySummary]] = UNSET
    """The monthly summaries of the transactions that fall into the ``BANK_PENALTIES`` credit category within the given
    time window, across all the accounts in the report."""

    days_since_last_occurrence: OptionalNullable[int] = UNSET
    """The number of days since the last transaction that falls into the ``BANK_PENALTIES`` credit category, across all
    the accounts in the report."""

    percentage_of_income: OptionalNullable[float] = UNSET
    """The percentage of the user's monthly inflows that was spent on transactions that fall into the ``BANK_PENALTIES``
    credit category within the given time window, across all the accounts in the report. For example, a value of 100
    represents that 100% of the inflows were spent on transactions that fall into the ``BANK_PENALTIES`` credit
    category. If there's no available income for the given time period, this field value will be ``-1``."""


class BankPenaltiesIndicatorsDict(TypedDict):
    amount: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    monthly_average: NotRequired[MonthlyAverage | MonthlyAverageDict | None]
    category_details: NotRequired[list[CategoryExpenses | CategoryExpensesDict] | None]
    transactions_count: NotRequired[int | None]
    monthly_summaries: NotRequired[list[MonthlySummary | MonthlySummaryDict] | None]
    days_since_last_occurrence: NotRequired[int | None]
    percentage_of_income: NotRequired[float | None]
