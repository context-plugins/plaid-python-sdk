from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class UserDataOverview(SdkBaseModel):
    """metadata for the set of insights provided in ``TransactionsUserInsightsGetResponse``"""

    transaction_count: int
    """The total number of transactions."""

    oldest_transaction_date: Optional[Date] = UNSET
    """The date of the oldest transaction processed to generate insights."""

    newest_transaction_date: Optional[Date] = UNSET
    """The date of the newest transaction processed to generate insights."""

    days_available: int
    """The range of days of transactions available."""

    total_outflows: float
    """Sum of outflow amounts."""

    total_inflows: float
    """Sum of inflow amounts."""


class UserDataOverviewDict(TypedDict):
    transaction_count: int
    oldest_transaction_date: NotRequired[Date]
    newest_transaction_date: NotRequired[Date]
    days_available: int
    total_outflows: float
    total_inflows: float
