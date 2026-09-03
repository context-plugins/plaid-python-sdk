from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class HistoricalAnnualIncome(SdkBaseModel):
    """An object representing the historical annual income amount."""

    baseline_amount: OptionalNullable[float] = UNSET
    """The historical annual income at the time of subscription"""

    current_amount: float
    """The current historical annual income"""


class HistoricalAnnualIncomeDict(TypedDict):
    baseline_amount: NotRequired[float | None]
    current_amount: float
