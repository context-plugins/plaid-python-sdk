from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WatchlistScreeningEntityProgramGetRequest(SdkBaseModel):
    """Request input for fetching an entity watchlist program"""

    entity_watchlist_program_id: str
    """ID of the associated entity program."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""


class WatchlistScreeningEntityProgramGetRequestDict(TypedDict):
    entity_watchlist_program_id: str
    secret: NotRequired[str]
    client_id: NotRequired[str]
