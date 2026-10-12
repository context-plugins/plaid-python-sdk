from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .amount_with_currency import AmountWithCurrency, AmountWithCurrencyDict
from .category_expenses import CategoryExpenses, CategoryExpensesDict


class OutlierTransactionsInsights(SdkBaseModel):
    """Insights into unusually large transactions that exceed typical spending patterns for the account."""

    transactions_count: OptionalNullable[int] = UNSET
    """The total number of transactions whose value is above the threshold of normal amounts for a given account."""

    total_amount: OptionalNullable[AmountWithCurrency] = UNSET
    """A monetary amount with its associated currency information, supporting both official and unofficial currency
    codes."""

    top_categories: Optional[list[CategoryExpenses | None]] = UNSET
    """Up to 3 top categories of expenses in this group."""


class OutlierTransactionsInsightsDict(TypedDict):
    transactions_count: NotRequired[int | None]
    total_amount: NotRequired[AmountWithCurrencyDict | None]
    top_categories: NotRequired[list[CategoryExpensesDict | None]]
