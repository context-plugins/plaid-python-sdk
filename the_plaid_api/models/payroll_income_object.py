from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit1099 import Credit1099, Credit1099Dict
from .credit_i20 import CreditI20, CreditI20Dict
from .credit_pay_stub import CreditPayStub, CreditPayStubDict
from .credit_w2 import CreditW2, CreditW2Dict


class PayrollIncomeObject(SdkBaseModel):
    """An object representing payroll data."""

    account_id: str | None
    """ID of the payroll provider account."""

    pay_stubs: list[CreditPayStub]
    """Array of pay stubs for the user."""

    w2s: list[CreditW2]
    """Array of tax form W-2s."""

    form1099s: list[Credit1099]
    """Array of tax form 1099s."""

    i20s: list[CreditI20]
    """Array of Form I-20 US immigration student documents."""


class PayrollIncomeObjectDict(TypedDict):
    account_id: str | None
    pay_stubs: list[CreditPayStub | CreditPayStubDict]
    w2s: list[CreditW2 | CreditW2Dict]
    form1099s: list[Credit1099 | Credit1099Dict]
    i20s: list[CreditI20 | CreditI20Dict]
