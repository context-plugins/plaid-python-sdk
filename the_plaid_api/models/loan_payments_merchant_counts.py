from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class LoanPaymentsMerchantCounts(SdkBaseModel):
    """Details regarding the number of unique loan payment merchants"""

    baseline_count: OptionalNullable[float] = UNSET
    """The number of unique loan payment merchants detected in the 30 days before the subscription date"""

    current_count: float
    """The current number of unique loan payment merchants detected in the last 30 days"""


class LoanPaymentsMerchantCountsDict(TypedDict):
    baseline_count: NotRequired[float | None]
    current_count: float
