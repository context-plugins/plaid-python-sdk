from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel


class BaseReportLongestGapInsights(SdkBaseModel):
    """Largest number of days between sequential transactions per calendar month"""

    start_date: Optional[Date] = UNSET
    """The start date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Optional[Date] = UNSET
    """The end date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    days: OptionalNullable[int] = UNSET
    """Largest number of days between sequential transactions for this time period."""


class BaseReportLongestGapInsightsDict(TypedDict):
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    days: NotRequired[int | None]
