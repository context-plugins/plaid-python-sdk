from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .entity_document import EntityDocument, EntityDocumentDict
from .match_summary import MatchSummary, MatchSummaryDict


class EntityScreeningHitDocumentsItems(SdkBaseModel):
    """Analyzed documents for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[EntityDocument] = UNSET
    """An official document, usually issued by a governing body or institution, with an associated identifier."""


class EntityScreeningHitDocumentsItemsDict(TypedDict):
    analysis: NotRequired[MatchSummary | MatchSummaryDict]
    data: NotRequired[EntityDocument | EntityDocumentDict]
