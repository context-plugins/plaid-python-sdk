from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .monthly_average import MonthlyAverage, MonthlyAverageDict


class CategoryExpenses(SdkBaseModel):
    """Detailed expense information for a specific credit category, including transaction count and total amount
    spent."""

    id: Optional[str] = UNSET
    """The ID of the credit category.

    See the `category taxonomy <https://plaid.com/documents/credit-category-taxonomy.csv>`__ for a full listing of
    category IDs."""

    transactions_count: OptionalNullable[int] = UNSET
    """The total number of transactions that fall into this credit category within the given time window."""

    amount: OptionalNullable[float] = UNSET
    """The total value for all the transactions that fall into this category within the given time window."""

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


class CategoryExpensesDict(TypedDict):
    id: NotRequired[str]
    transactions_count: NotRequired[int | None]
    amount: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    monthly_average: NotRequired[MonthlyAverage | MonthlyAverageDict | None]
