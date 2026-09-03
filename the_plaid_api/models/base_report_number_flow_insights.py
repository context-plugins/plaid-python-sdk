from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class BaseReportNumberFlowInsights(SdkBaseModel):
    """The number of credits or debits out of the account. This field will only be included for depository accounts."""

    start_date: Date
    """The start date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Date
    """The end date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    count: int
    """The number of credits or debits out of the account for this time period."""


class BaseReportNumberFlowInsightsDict(TypedDict):
    start_date: Date
    end_date: Date
    count: int
