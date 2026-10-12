from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .cra_verification_income_metrics import CraVerificationIncomeMetrics, CraVerificationIncomeMetricsDict
from .cra_verification_income_stream_insights import (
    CraVerificationIncomeStreamInsights,
    CraVerificationIncomeStreamInsightsDict,
)
from .cra_verification_income_transaction import CraVerificationIncomeTransaction, CraVerificationIncomeTransactionDict


class CraVerificationIncomeStream(SdkBaseModel):
    """An income stream detected for the user."""

    income_stream_id: str
    """A unique identifier for an income stream. If the report is regenerated and a new ``report_id`` is created, the
    new report will have a new set of ``income_stream_id``s."""

    start_date: Date
    """Minimum of all dates within the specific income stream for days requested by the client. The date will be
    returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Date
    """Maximum of all dates within the specific income stream for days requested by the client. The date will be
    returned in an ISO 8601 format (YYYY-MM-DD)."""

    description: str
    """The most common name or original description for the underlying income transactions."""

    insights: CraVerificationIncomeStreamInsights
    """Modeled insights for a given income stream."""

    income_metrics: CraVerificationIncomeMetrics
    """Modeled income metrics for a given income stream or user summary."""

    transactions: list[CraVerificationIncomeTransaction]
    """The transactions data for the income stream ordered by ascending date."""


class CraVerificationIncomeStreamDict(TypedDict):
    income_stream_id: str
    start_date: Date
    end_date: Date
    description: str
    insights: CraVerificationIncomeStreamInsightsDict
    income_metrics: CraVerificationIncomeMetricsDict
    transactions: list[CraVerificationIncomeTransactionDict]
