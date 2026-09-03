from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .match_summary import MatchSummary, MatchSummaryDict
from .watchlist_screening_hit_locations import WatchlistScreeningHitLocations, WatchlistScreeningHitLocationsDict


class GenericScreeningHitLocationItems(SdkBaseModel):
    """Analyzed location information for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[WatchlistScreeningHitLocations] = UNSET
    """Location information for the associated watchlist hit"""


class GenericScreeningHitLocationItemsDict(TypedDict):
    analysis: NotRequired[MatchSummary | MatchSummaryDict]
    data: NotRequired[WatchlistScreeningHitLocations | WatchlistScreeningHitLocationsDict]
