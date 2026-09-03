from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .cra_income_metrics import CraIncomeMetrics, CraIncomeMetricsDict
from .cra_income_stream_insights import CraIncomeStreamInsights, CraIncomeStreamInsightsDict
from .cra_income_transaction import CraIncomeTransaction, CraIncomeTransactionDict


class CraIncomeStream(SdkBaseModel):
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

    insights: CraIncomeStreamInsights
    """Modeled insights for a given income stream."""

    income_metrics: CraIncomeMetrics
    """Modeled income metrics for a given income stream or user summary."""

    transactions: list[CraIncomeTransaction]
    """The transactions data for the income stream ordered by ascending date."""


class CraIncomeStreamDict(TypedDict):
    income_stream_id: str
    start_date: Date
    end_date: Date
    description: str
    insights: CraIncomeStreamInsights | CraIncomeStreamInsightsDict
    income_metrics: CraIncomeMetrics | CraIncomeMetricsDict
    transactions: list[CraIncomeTransaction | CraIncomeTransactionDict]
