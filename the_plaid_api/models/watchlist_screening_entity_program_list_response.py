from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .entity_watchlist_program import EntityWatchlistProgram, EntityWatchlistProgramDict


class WatchlistScreeningEntityProgramListResponse(SdkBaseModel):
    """Paginated list of entity watchlist screening programs"""

    entity_watchlist_programs: list[EntityWatchlistProgram]
    """List of entity watchlist screening programs"""

    next_cursor: str | None
    """An identifier that determines which page of results you receive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WatchlistScreeningEntityProgramListResponseDict(TypedDict):
    entity_watchlist_programs: list[EntityWatchlistProgram | EntityWatchlistProgramDict]
    next_cursor: str | None
    request_id: str
