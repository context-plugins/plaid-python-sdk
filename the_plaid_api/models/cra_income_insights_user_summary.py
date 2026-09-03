from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_income_metrics import CraIncomeMetrics, CraIncomeMetricsDict


class CraIncomeInsightsUserSummary(SdkBaseModel):
    """Aggregated summary of all income streams for this user."""

    income_metrics: list[CraIncomeMetrics]
    """List of a user's aggregated income metrics for each currency."""


class CraIncomeInsightsUserSummaryDict(TypedDict):
    income_metrics: list[CraIncomeMetrics | CraIncomeMetricsDict]
