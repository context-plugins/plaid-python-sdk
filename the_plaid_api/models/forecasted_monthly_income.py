from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ForecastedMonthlyIncome(SdkBaseModel):
    """An object representing the predicted average monthly net income amount. This amount reflects the funds deposited
    into the account and may not include any withheld income such as taxes or other payroll deductions"""

    baseline_amount: OptionalNullable[float] = UNSET
    """The forecasted monthly income at the time of subscription"""

    current_amount: float
    """The current forecasted monthly income"""


class ForecastedMonthlyIncomeDict(TypedDict):
    baseline_amount: NotRequired[float | None]
    current_amount: float
