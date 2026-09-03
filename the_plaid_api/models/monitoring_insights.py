from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .monitoring_income_insights import MonitoringIncomeInsights, MonitoringIncomeInsightsDict
from .monitoring_loan_insights import MonitoringLoanInsights, MonitoringLoanInsightsDict


class MonitoringInsights(SdkBaseModel):
    """An object representing the Monitoring Insights for the given Item"""

    income: MonitoringIncomeInsights
    """An object representing the income subcategory of the report"""

    loans: MonitoringLoanInsights
    """An object representing the loan exposure subcategory of the report"""


class MonitoringInsightsDict(TypedDict):
    income: MonitoringIncomeInsights | MonitoringIncomeInsightsDict
    loans: MonitoringLoanInsights | MonitoringLoanInsightsDict
