from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .deductions_breakdown import DeductionsBreakdown, DeductionsBreakdownDict
from .deductions_total import DeductionsTotal, DeductionsTotalDict
from .total import Total, TotalDict


class Deductions(SdkBaseModel):
    """An object with the deduction information found on a paystub."""

    subtotals: Optional[list[Total]] = UNSET
    breakdown: list[DeductionsBreakdown]
    totals: Optional[list[Total]] = UNSET
    total: DeductionsTotal
    """An object representing the total deductions for the pay period"""


class DeductionsDict(TypedDict):
    subtotals: NotRequired[list[Total | TotalDict]]
    breakdown: list[DeductionsBreakdown | DeductionsBreakdownDict]
    totals: NotRequired[list[Total | TotalDict]]
    total: DeductionsTotal | DeductionsTotalDict
