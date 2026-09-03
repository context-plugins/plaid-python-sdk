from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class WatchlistScreeningIndividualHitListRequest(SdkBaseModel):
    """Request input for listing hits for an individual watchlist screening"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    watchlist_screening_id: str
    """ID of the associated screening."""

    cursor: OptionalNullable[str] = UNSET
    """An identifier that determines which page of results you receive."""


class WatchlistScreeningIndividualHitListRequestDict(TypedDict):
    secret: NotRequired[str]
    client_id: NotRequired[str]
    watchlist_screening_id: str
    cursor: NotRequired[str | None]
