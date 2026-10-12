from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .individual_screening_hit_names import IndividualScreeningHitNames, IndividualScreeningHitNamesDict
from .match_summary import MatchSummary, MatchSummaryDict


class ScreeningHitNamesItems(SdkBaseModel):
    """Analyzed name information for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[IndividualScreeningHitNames] = UNSET
    """Name information for the associated individual watchlist hit"""


class ScreeningHitNamesItemsDict(TypedDict):
    analysis: NotRequired[MatchSummaryDict]
    data: NotRequired[IndividualScreeningHitNamesDict]
