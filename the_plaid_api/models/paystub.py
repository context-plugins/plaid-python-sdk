from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .deductions import Deductions, DeductionsDict
from .earnings import Earnings, EarningsDict
from .employee import Employee, EmployeeDict
from .employment_details import EmploymentDetails, EmploymentDetailsDict
from .income_breakdown import IncomeBreakdown, IncomeBreakdownDict
from .net_pay import NetPay, NetPayDict
from .pay_period_details import PayPeriodDetails, PayPeriodDetailsDict
from .paystub_details import PaystubDetails, PaystubDetailsDict
from .paystub_employer import PaystubEmployer, PaystubEmployerDict
from .paystub_ytddetails import PaystubYtddetails, PaystubYtddetailsDict


class Paystub(SdkBaseModel):
    """An object representing data extracted from the end user's paystub."""

    deductions: Deductions
    """An object with the deduction information found on a paystub."""

    doc_id: str
    """An identifier of the document referenced by the document metadata."""

    earnings: Earnings
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""

    employee: Employee
    """Data about the employee."""

    employer: PaystubEmployer
    """Information about the employer on the paystub"""

    employment_details: Optional[EmploymentDetails] = UNSET
    """An object representing employment details found on a paystub."""

    net_pay: NetPay
    """An object representing information about the net pay amount on the paystub."""

    pay_period_details: PayPeriodDetails
    """Details about the pay period."""

    paystub_details: Optional[PaystubDetails] = UNSET
    """An object representing details that can be found on the paystub."""

    income_breakdown: Optional[list[IncomeBreakdown]] = UNSET
    ytd_earnings: Optional[PaystubYtddetails] = UNSET
    """The amount of income earned year to date, as based on paystub data."""


class PaystubDict(TypedDict):
    deductions: Deductions | DeductionsDict
    doc_id: str
    earnings: Earnings | EarningsDict
    employee: Employee | EmployeeDict
    employer: PaystubEmployer | PaystubEmployerDict
    employment_details: NotRequired[EmploymentDetails | EmploymentDetailsDict]
    net_pay: NetPay | NetPayDict
    pay_period_details: PayPeriodDetails | PayPeriodDetailsDict
    paystub_details: NotRequired[PaystubDetails | PaystubDetailsDict]
    income_breakdown: NotRequired[list[IncomeBreakdown | IncomeBreakdownDict]]
    ytd_earnings: NotRequired[PaystubYtddetails | PaystubYtddetailsDict]
