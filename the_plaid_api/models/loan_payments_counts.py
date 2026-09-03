from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class LoanPaymentsCounts(SdkBaseModel):
    """Details regarding the number of loan payments"""

    baseline_count: OptionalNullable[float] = UNSET
    """The number of loan payments made in the 30 days before the subscription date"""

    current_count: float
    """The current number of loan payments made in the last 30 days"""


class LoanPaymentsCountsDict(TypedDict):
    baseline_count: NotRequired[float | None]
    current_count: float
