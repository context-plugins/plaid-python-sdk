from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .category_expenses import CategoryExpenses, CategoryExpensesDict
from .monthly_average import MonthlyAverage, MonthlyAverageDict


class ExpenditureSummary(SdkBaseModel):
    """Summary statistics for a specific expenditure category, including total amount, monthly average, and percentage
    of income."""

    amount: OptionalNullable[float] = UNSET
    """The total value of all the aggregated transactions in this expenditure category."""

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

    transactions_count: OptionalNullable[int] = UNSET
    """The total number of outflow transactions in this expenses group, within the given time window across all the
    accounts in the report."""

    percentage_of_income: OptionalNullable[float] = UNSET
    """The percentage of the total inflows that was spent in this expenses group, within the given time window across
    all the accounts in the report. For example, a value of 100 represents that 100% of the inflows were spent on
    transactions that fall into this expenditure group. If there's no available income for the given time period, this
    field value will be ``-1``."""

    top_categories: Optional[list[CategoryExpenses | None]] = UNSET
    """The primary credit categories of the expenses within the given time window, across all the accounts in the
    report.

    The categories are sorted in descending order by the total value spent. See the `category taxonomy
    <https://plaid.com/documents/credit-category-taxonomy.csv>`__ for a full listing of category IDs."""


class ExpenditureSummaryDict(TypedDict):
    amount: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    monthly_average: NotRequired[MonthlyAverageDict | None]
    transactions_count: NotRequired[int | None]
    percentage_of_income: NotRequired[float | None]
    top_categories: NotRequired[list[CategoryExpensesDict | None]]
