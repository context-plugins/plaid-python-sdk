from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paystub_override_deductions_breakdown import (
    PaystubOverrideDeductionsBreakdown,
    PaystubOverrideDeductionsBreakdownDict,
)
from .paystub_override_deductions_total import PaystubOverrideDeductionsTotal, PaystubOverrideDeductionsTotalDict


class PaystubOverrideDeductions(SdkBaseModel):
    """An object with the deduction information found on a paystub."""

    breakdown: Optional[list[PaystubOverrideDeductionsBreakdown]] = UNSET
    total: Optional[PaystubOverrideDeductionsTotal] = UNSET
    """An object representing the total deductions for the pay period"""


class PaystubOverrideDeductionsDict(TypedDict):
    breakdown: NotRequired[list[PaystubOverrideDeductionsBreakdown | PaystubOverrideDeductionsBreakdownDict]]
    total: NotRequired[PaystubOverrideDeductionsTotal | PaystubOverrideDeductionsTotalDict]
