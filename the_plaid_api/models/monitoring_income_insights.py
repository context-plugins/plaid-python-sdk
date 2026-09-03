from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .forecasted_monthly_income import ForecastedMonthlyIncome, ForecastedMonthlyIncomeDict
from .historical_annual_income import HistoricalAnnualIncome, HistoricalAnnualIncomeDict
from .income_sources_counts import IncomeSourcesCounts, IncomeSourcesCountsDict
from .monitoring_income_source import MonitoringIncomeSource, MonitoringIncomeSourceDict
from .total_monthly_income_insights import TotalMonthlyIncomeInsights, TotalMonthlyIncomeInsightsDict


class MonitoringIncomeInsights(SdkBaseModel):
    """An object representing the income subcategory of the report"""

    total_monthly_income: TotalMonthlyIncomeInsights
    """Details about the total monthly income"""

    income_sources_counts: IncomeSourcesCounts
    """Details about the number of income sources"""

    forecasted_monthly_income: ForecastedMonthlyIncome
    """An object representing the predicted average monthly net income amount. This amount reflects the funds deposited
    into the account and may not include any withheld income such as taxes or other payroll deductions"""

    historical_annual_income: HistoricalAnnualIncome
    """An object representing the historical annual income amount."""

    income_sources: list[MonitoringIncomeSource]
    """The income sources for this Item. Each entry in the array is a single income source"""


class MonitoringIncomeInsightsDict(TypedDict):
    total_monthly_income: TotalMonthlyIncomeInsights | TotalMonthlyIncomeInsightsDict
    income_sources_counts: IncomeSourcesCounts | IncomeSourcesCountsDict
    forecasted_monthly_income: ForecastedMonthlyIncome | ForecastedMonthlyIncomeDict
    historical_annual_income: HistoricalAnnualIncome | HistoricalAnnualIncomeDict
    income_sources: list[MonitoringIncomeSource | MonitoringIncomeSourceDict]
