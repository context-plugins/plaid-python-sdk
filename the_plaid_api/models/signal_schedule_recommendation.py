from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.recommendation_string import RecommendationStringOrStr


class SignalScheduleRecommendation(SdkBaseModel):
    """Conveys information on if a retry is recommended on a given date"""

    date: Optional[Date] = UNSET
    """The specific date for submitting the debit entry, formatted in ISO 8601 (e.g., "2025-01-17")."""

    recommendation: Optional[RecommendationStringOrStr] = UNSET
    """The recommendation result for that date."""

    rank: OptionalNullable[int] = UNSET
    """The rank of the recommendation based on the likelihood of debit success, with 1 representing the most optimal
    date. Dates with ``NOT_RECOMMENDED`` or ``UNKNOWN`` will have rank ``null``."""


class SignalScheduleRecommendationDict(TypedDict):
    date: NotRequired[Date]
    recommendation: NotRequired[RecommendationStringOrStr]
    rank: NotRequired[int | None]
