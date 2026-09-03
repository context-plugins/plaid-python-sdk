from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .individual_watchlist_program import IndividualWatchlistProgram, IndividualWatchlistProgramDict


class WatchlistScreeningIndividualProgramListResponse(SdkBaseModel):
    """Paginated list of individual watchlist screening programs"""

    watchlist_programs: list[IndividualWatchlistProgram]
    """List of individual watchlist screening programs"""

    next_cursor: str | None
    """An identifier that determines which page of results you receive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WatchlistScreeningIndividualProgramListResponseDict(TypedDict):
    watchlist_programs: list[IndividualWatchlistProgram | IndividualWatchlistProgramDict]
    next_cursor: str | None
    request_id: str
