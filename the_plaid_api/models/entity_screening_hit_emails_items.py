from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .entity_screening_hit_emails import EntityScreeningHitEmails, EntityScreeningHitEmailsDict
from .match_summary import MatchSummary, MatchSummaryDict


class EntityScreeningHitEmailsItems(SdkBaseModel):
    """Analyzed emails for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[EntityScreeningHitEmails] = UNSET
    """Email address information for the associated entity watchlist hit"""


class EntityScreeningHitEmailsItemsDict(TypedDict):
    analysis: NotRequired[MatchSummary | MatchSummaryDict]
    data: NotRequired[EntityScreeningHitEmails | EntityScreeningHitEmailsDict]
