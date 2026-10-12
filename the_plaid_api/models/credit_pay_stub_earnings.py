from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pay_stub_earnings_breakdown import PayStubEarningsBreakdown, PayStubEarningsBreakdownDict
from .pay_stub_earnings_total import PayStubEarningsTotal, PayStubEarningsTotalDict


class CreditPayStubEarnings(SdkBaseModel):
    """An object representing both a breakdown of earnings on a pay stub and the total earnings."""

    breakdown: list[PayStubEarningsBreakdown]
    total: PayStubEarningsTotal
    """An object representing both the current pay period and year to date amount for an earning category."""


class CreditPayStubEarningsDict(TypedDict):
    breakdown: list[PayStubEarningsBreakdownDict]
    total: PayStubEarningsTotalDict
