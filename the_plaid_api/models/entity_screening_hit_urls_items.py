from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .entity_screening_hit_urls import EntityScreeningHitUrls, EntityScreeningHitUrlsDict
from .match_summary import MatchSummary, MatchSummaryDict


class EntityScreeningHitUrlsItems(SdkBaseModel):
    """Analyzed URLs for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[EntityScreeningHitUrls] = UNSET
    """URLs associated with the entity screening hit"""


class EntityScreeningHitUrlsItemsDict(TypedDict):
    analysis: NotRequired[MatchSummaryDict]
    data: NotRequired[EntityScreeningHitUrlsDict]
