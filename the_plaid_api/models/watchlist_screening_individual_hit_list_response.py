from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .watchlist_screening_hit import WatchlistScreeningHit, WatchlistScreeningHitDict


class WatchlistScreeningIndividualHitListResponse(SdkBaseModel):
    """Paginated list of individual watchlist screening hits"""

    watchlist_screening_hits: list[WatchlistScreeningHit]
    """List of individual watchlist screening hits"""

    next_cursor: str | None
    """An identifier that determines which page of results you receive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WatchlistScreeningIndividualHitListResponseDict(TypedDict):
    watchlist_screening_hits: list[WatchlistScreeningHitDict]
    next_cursor: str | None
    request_id: str
