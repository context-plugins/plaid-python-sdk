from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class IncomeSourcesCounts(SdkBaseModel):
    """Details about the number of income sources"""

    baseline_count: OptionalNullable[float] = UNSET
    """The number of income sources detected at the subscription date"""

    current_count: float
    """The number of income sources currently detected"""


class IncomeSourcesCountsDict(TypedDict):
    baseline_count: NotRequired[float | None]
    current_count: float
