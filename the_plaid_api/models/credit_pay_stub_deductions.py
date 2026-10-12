from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pay_stub_deductions_breakdown import PayStubDeductionsBreakdown, PayStubDeductionsBreakdownDict
from .pay_stub_deductions_total import PayStubDeductionsTotal, PayStubDeductionsTotalDict


class CreditPayStubDeductions(SdkBaseModel):
    """An object with the deduction information found on a pay stub."""

    breakdown: list[PayStubDeductionsBreakdown]
    total: PayStubDeductionsTotal
    """An object representing the total deductions for the pay period"""


class CreditPayStubDeductionsDict(TypedDict):
    breakdown: list[PayStubDeductionsBreakdownDict]
    total: PayStubDeductionsTotalDict
