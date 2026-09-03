from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TotalMonthlyIncomeInsights(SdkBaseModel):
    """Details about the total monthly income"""

    baseline_amount: OptionalNullable[float] = UNSET
    """The aggregated income for the 30 days prior to subscription date"""

    current_amount: float
    """The aggregated income of the last 30 days"""


class TotalMonthlyIncomeInsightsDict(TypedDict):
    baseline_amount: NotRequired[float | None]
    current_amount: float
