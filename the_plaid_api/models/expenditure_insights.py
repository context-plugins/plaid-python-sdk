from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .amount_with_currency_with_monthly_average import (
    AmountWithCurrencyWithMonthlyAverage,
    AmountWithCurrencyWithMonthlyAverageDict,
)
from .expenditure_summary import ExpenditureSummary, ExpenditureSummaryDict
from .outlier_transactions_insights import OutlierTransactionsInsights, OutlierTransactionsInsightsDict


class ExpenditureInsights(SdkBaseModel):
    """Comprehensive analysis of spending patterns, categorizing expenses into essential, non-essential, and other
    categories."""

    cash_flow: OptionalNullable[AmountWithCurrencyWithMonthlyAverage] = UNSET
    """Net cash flow for the period (inflows minus outflows), including a monthly average."""

    total_expenditure: OptionalNullable[ExpenditureSummary] = UNSET
    """Summary statistics for a specific expenditure category, including total amount, monthly average, and percentage
    of income."""

    essential_expenditure: OptionalNullable[ExpenditureSummary] = UNSET
    """Summary statistics for a specific expenditure category, including total amount, monthly average, and percentage
    of income."""

    non_essential_expenditure: OptionalNullable[ExpenditureSummary] = UNSET
    """Summary statistics for a specific expenditure category, including total amount, monthly average, and percentage
    of income."""

    other: OptionalNullable[ExpenditureSummary] = UNSET
    """Summary statistics for a specific expenditure category, including total amount, monthly average, and percentage
    of income."""

    transfers_out: OptionalNullable[ExpenditureSummary] = UNSET
    """Summary statistics for a specific expenditure category, including total amount, monthly average, and percentage
    of income."""

    outlier_transactions: OptionalNullable[OutlierTransactionsInsights] = UNSET
    """Insights into unusually large transactions that exceed typical spending patterns for the account."""


class ExpenditureInsightsDict(TypedDict):
    cash_flow: NotRequired[AmountWithCurrencyWithMonthlyAverage | AmountWithCurrencyWithMonthlyAverageDict | None]
    total_expenditure: NotRequired[ExpenditureSummary | ExpenditureSummaryDict | None]
    essential_expenditure: NotRequired[ExpenditureSummary | ExpenditureSummaryDict | None]
    non_essential_expenditure: NotRequired[ExpenditureSummary | ExpenditureSummaryDict | None]
    other: NotRequired[ExpenditureSummary | ExpenditureSummaryDict | None]
    transfers_out: NotRequired[ExpenditureSummary | ExpenditureSummaryDict | None]
    outlier_transactions: NotRequired[OutlierTransactionsInsights | OutlierTransactionsInsightsDict | None]
