from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payroll_income_rate_of_pay import PayrollIncomeRateOfPay, PayrollIncomeRateOfPayDict


class PayrollIncomeAccountData(SdkBaseModel):
    """An object containing account level data."""

    account_id: str | None
    """ID of the payroll provider account."""

    rate_of_pay: PayrollIncomeRateOfPay
    """An object representing the rate at which an individual is paid."""

    pay_frequency: str | None
    """The frequency at which an individual is paid."""


class PayrollIncomeAccountDataDict(TypedDict):
    account_id: str | None
    rate_of_pay: PayrollIncomeRateOfPayDict
    pay_frequency: str | None
