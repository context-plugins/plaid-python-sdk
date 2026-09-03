from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .date_range import DateRange, DateRangeDict
from .match_summary import MatchSummary, MatchSummaryDict


class ScreeningHitDateOfBirthItem(SdkBaseModel):
    """Analyzed date of birth for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[DateRange] = UNSET
    """A date range with a start and end date"""


class ScreeningHitDateOfBirthItemDict(TypedDict):
    analysis: NotRequired[MatchSummary | MatchSummaryDict]
    data: NotRequired[DateRange | DateRangeDict]
