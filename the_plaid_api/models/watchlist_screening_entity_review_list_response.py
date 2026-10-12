from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .entity_watchlist_screening_review import EntityWatchlistScreeningReview, EntityWatchlistScreeningReviewDict


class WatchlistScreeningEntityReviewListResponse(SdkBaseModel):
    """Paginated list of entity watchlist screening reviews"""

    entity_watchlist_screening_reviews: list[EntityWatchlistScreeningReview]
    """List of entity watchlist screening reviews"""

    next_cursor: str | None
    """An identifier that determines which page of results you receive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WatchlistScreeningEntityReviewListResponseDict(TypedDict):
    entity_watchlist_screening_reviews: list[EntityWatchlistScreeningReviewDict]
    next_cursor: str | None
    request_id: str
