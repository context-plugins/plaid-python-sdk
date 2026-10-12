from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .base_report_transaction import BaseReportTransaction, BaseReportTransactionDict


class CraVoaReportTransactionsInsights(SdkBaseModel):
    """Transaction data associated with the account."""

    all_transactions: list[BaseReportTransaction]
    """Transaction history associated with the account."""

    end_date: Date | None
    """The latest timeframe provided by the FI, in an ISO 8601 format (YYYY-MM-DD)."""

    start_date: Date | None
    """The earliest timeframe provided by the FI, in an ISO 8601 format (YYYY-MM-DD)."""


class CraVoaReportTransactionsInsightsDict(TypedDict):
    all_transactions: list[BaseReportTransactionDict]
    end_date: Date | None
    start_date: Date | None
