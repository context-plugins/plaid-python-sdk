from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class WatchlistScreeningEntityProgramListRequest(SdkBaseModel):
    """Request input for listing entity watchlist screening programs"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    cursor: OptionalNullable[str] = UNSET
    """An identifier that determines which page of results you receive."""


class WatchlistScreeningEntityProgramListRequestDict(TypedDict):
    secret: NotRequired[str]
    client_id: NotRequired[str]
    cursor: NotRequired[str | None]
