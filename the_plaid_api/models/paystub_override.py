from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .income_breakdown import IncomeBreakdown, IncomeBreakdownDict
from .paystub_override_deductions import PaystubOverrideDeductions, PaystubOverrideDeductionsDict
from .paystub_override_earnings import PaystubOverrideEarnings, PaystubOverrideEarningsDict
from .paystub_override_employee import PaystubOverrideEmployee, PaystubOverrideEmployeeDict
from .paystub_override_employer import PaystubOverrideEmployer, PaystubOverrideEmployerDict
from .paystub_override_net_pay import PaystubOverrideNetPay, PaystubOverrideNetPayDict
from .paystub_override_pay_period_details import PaystubOverridePayPeriodDetails, PaystubOverridePayPeriodDetailsDict


class PaystubOverride(SdkBaseModel):
    """An object representing data from a paystub."""

    employer: Optional[PaystubOverrideEmployer] = UNSET
    """The employer on the paystub."""

    employee: Optional[PaystubOverrideEmployee] = UNSET
    """The employee on the paystub."""

    income_breakdown: Optional[list[IncomeBreakdown]] = UNSET
    net_pay: Optional[PaystubOverrideNetPay] = UNSET
    """An object representing information about the net pay amount on the paystub."""

    deductions: Optional[PaystubOverrideDeductions] = UNSET
    """An object with the deduction information found on a paystub."""

    earnings: Optional[PaystubOverrideEarnings] = UNSET
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""

    pay_period_details: Optional[PaystubOverridePayPeriodDetails] = UNSET
    """Details about the pay period."""


class PaystubOverrideDict(TypedDict):
    employer: NotRequired[PaystubOverrideEmployer | PaystubOverrideEmployerDict]
    employee: NotRequired[PaystubOverrideEmployee | PaystubOverrideEmployeeDict]
    income_breakdown: NotRequired[list[IncomeBreakdown | IncomeBreakdownDict]]
    net_pay: NotRequired[PaystubOverrideNetPay | PaystubOverrideNetPayDict]
    deductions: NotRequired[PaystubOverrideDeductions | PaystubOverrideDeductionsDict]
    earnings: NotRequired[PaystubOverrideEarnings | PaystubOverrideEarningsDict]
    pay_period_details: NotRequired[PaystubOverridePayPeriodDetails | PaystubOverridePayPeriodDetailsDict]
