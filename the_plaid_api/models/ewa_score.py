from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EwaScore(SdkBaseModel):
    """EwaScore represents an earned wage access score for a specific advance amount range."""

    lowest_amount: Optional[float] = UNSET
    """Float value representing the lower bound (inclusive) of the advance amount range associated with a specific EWA
    score."""

    highest_amount: Optional[float] = UNSET
    """Float value representing the upper bound (exclusive) of the advance amount range associated with a specific EWA
    score."""

    score: Optional[int] = UNSET
    """EWA score for the corresponding amount bucket. Scores range from 1-99, where a higher score indicates a higher
    likelihood of repayment."""


class EwaScoreDict(TypedDict):
    lowest_amount: NotRequired[float]
    highest_amount: NotRequired[float]
    score: NotRequired[int]
