from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paystub_override_earnings_breakdown import PaystubOverrideEarningsBreakdown, PaystubOverrideEarningsBreakdownDict
from .paystub_override_earnings_total import PaystubOverrideEarningsTotal, PaystubOverrideEarningsTotalDict


class PaystubOverrideEarnings(SdkBaseModel):
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""

    breakdown: Optional[list[PaystubOverrideEarningsBreakdown]] = UNSET
    total: Optional[PaystubOverrideEarningsTotal] = UNSET
    """An object representing both the current pay period and year to date amount for an earning category."""


class PaystubOverrideEarningsDict(TypedDict):
    breakdown: NotRequired[list[PaystubOverrideEarningsBreakdownDict]]
    total: NotRequired[PaystubOverrideEarningsTotalDict]
