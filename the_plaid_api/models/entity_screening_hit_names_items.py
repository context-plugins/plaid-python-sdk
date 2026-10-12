from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .entity_screening_hit_names import EntityScreeningHitNames, EntityScreeningHitNamesDict
from .match_summary import MatchSummary, MatchSummaryDict


class EntityScreeningHitNamesItems(SdkBaseModel):
    """Analyzed names for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[EntityScreeningHitNames] = UNSET
    """Name information for the associated entity watchlist hit"""


class EntityScreeningHitNamesItemsDict(TypedDict):
    analysis: NotRequired[MatchSummaryDict]
    data: NotRequired[EntityScreeningHitNamesDict]
