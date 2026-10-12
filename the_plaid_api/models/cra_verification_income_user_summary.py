from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_verification_income_metrics import CraVerificationIncomeMetrics, CraVerificationIncomeMetricsDict


class CraVerificationIncomeUserSummary(SdkBaseModel):
    """Aggregated summary of all income streams for this user."""

    income_metrics: list[CraVerificationIncomeMetrics]
    """List of a user's aggregated income metrics for each currency."""


class CraVerificationIncomeUserSummaryDict(TypedDict):
    income_metrics: list[CraVerificationIncomeMetricsDict]
