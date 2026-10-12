from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .entity_screening_hit_phone_numbers import EntityScreeningHitPhoneNumbers, EntityScreeningHitPhoneNumbersDict
from .match_summary import MatchSummary, MatchSummaryDict


class EntityScreeningHitsPhoneNumberItems(SdkBaseModel):
    """Analyzed phone numbers for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[EntityScreeningHitPhoneNumbers] = UNSET
    """Phone number information associated with the entity screening hit"""


class EntityScreeningHitsPhoneNumberItemsDict(TypedDict):
    analysis: NotRequired[MatchSummaryDict]
    data: NotRequired[EntityScreeningHitPhoneNumbersDict]
