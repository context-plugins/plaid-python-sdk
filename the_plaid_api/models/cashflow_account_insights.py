from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cashflow_report_historical_balance import CashflowReportHistoricalBalance, CashflowReportHistoricalBalanceDict
from .cashflow_report_monthly_summary import CashflowReportMonthlySummary, CashflowReportMonthlySummaryDict


class CashflowAccountInsights(SdkBaseModel):
    """Insights on the account level. These are only returned for Credit and Depository type accounts."""

    historical_balances: list[CashflowReportHistoricalBalance]
    """Calculated data about the historical balances on the account.

    Available for ``credit`` and ``depository`` type accounts."""

    monthly_summaries: list[CashflowReportMonthlySummary]
    """Monthly summary statistics derived from transaction-level data."""


class CashflowAccountInsightsDict(TypedDict):
    historical_balances: list[CashflowReportHistoricalBalanceDict]
    monthly_summaries: list[CashflowReportMonthlySummaryDict]
