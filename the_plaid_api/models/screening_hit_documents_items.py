from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .match_summary import MatchSummary, MatchSummaryDict
from .watchlist_screening_document import WatchlistScreeningDocument, WatchlistScreeningDocumentDict


class ScreeningHitDocumentsItems(SdkBaseModel):
    """Analyzed document information for the associated hit"""

    analysis: Optional[MatchSummary] = UNSET
    """Summary object reflecting the match result of the associated data"""

    data: Optional[WatchlistScreeningDocument] = UNSET
    """An official document, usually issued by a governing body or institution, with an associated identifier."""


class ScreeningHitDocumentsItemsDict(TypedDict):
    analysis: NotRequired[MatchSummaryDict]
    data: NotRequired[WatchlistScreeningDocumentDict]
