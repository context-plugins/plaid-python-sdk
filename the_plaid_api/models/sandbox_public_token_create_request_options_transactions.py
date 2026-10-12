from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class SandboxPublicTokenCreateRequestOptionsTransactions(SdkBaseModel):
    """An optional set of parameters corresponding to transactions options."""

    start_date: Optional[Date] = UNSET
    """The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD."""

    end_date: Optional[Date] = UNSET
    """The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD."""

    days_requested: int = 90
    """The maximum number of days of transaction history to request for the Transactions product."""


class SandboxPublicTokenCreateRequestOptionsTransactionsDict(TypedDict):
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    days_requested: NotRequired[int]
