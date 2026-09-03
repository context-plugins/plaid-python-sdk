from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .earnings_breakdown import EarningsBreakdown, EarningsBreakdownDict
from .earnings_total import EarningsTotal, EarningsTotalDict


class Earnings(SdkBaseModel):
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""

    subtotals: Optional[list[EarningsTotal]] = UNSET
    totals: Optional[list[EarningsTotal]] = UNSET
    breakdown: Optional[list[EarningsBreakdown]] = UNSET
    total: Optional[EarningsTotal] = UNSET
    """An object representing both the current pay period and year to date amount for an earning category."""


class EarningsDict(TypedDict):
    subtotals: NotRequired[list[EarningsTotal | EarningsTotalDict]]
    totals: NotRequired[list[EarningsTotal | EarningsTotalDict]]
    breakdown: NotRequired[list[EarningsBreakdown | EarningsBreakdownDict]]
    total: NotRequired[EarningsTotal | EarningsTotalDict]
