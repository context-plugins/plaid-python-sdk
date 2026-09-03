from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PayrollIncomeRateOfPay(SdkBaseModel):
    """An object representing the rate at which an individual is paid."""

    pay_rate: OptionalNullable[str] = UNSET
    """The rate at which an employee is paid."""

    pay_amount: OptionalNullable[float] = UNSET
    """The amount at which an employee is paid."""


class PayrollIncomeRateOfPayDict(TypedDict):
    pay_rate: NotRequired[str | None]
    pay_amount: NotRequired[float | None]
