from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .recurring_insights_stream import RecurringInsightsStream, RecurringInsightsStreamDict


class RecurringTransactions(SdkBaseModel):
    """Insights object for recurring transactions for ``/beta/transactions/user_insights/v1/get`` endpoint"""

    inflow_streams: list[RecurringInsightsStream]
    """An array of inflow transaction streams (e.g., income)."""

    outflow_streams: list[RecurringInsightsStream]
    """An array of outflow transaction streams (e.g., subscriptions, bills, loan payments)."""


class RecurringTransactionsDict(TypedDict):
    inflow_streams: list[RecurringInsightsStreamDict]
    outflow_streams: list[RecurringInsightsStreamDict]
