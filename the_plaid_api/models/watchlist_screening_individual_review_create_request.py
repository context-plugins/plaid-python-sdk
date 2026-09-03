from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class WatchlistScreeningIndividualReviewCreateRequest(SdkBaseModel):
    """Request input for creating a screening review"""

    confirmed_hits: list[str]
    """Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once
    confirmed. In most cases, confirmed hits indicate that the customer should be rejected."""

    dismissed_hits: list[str]
    """Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once
    dismissed."""

    comment: OptionalNullable[str] = UNSET
    """A comment submitted by a team member as part of reviewing a watchlist screening."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    watchlist_screening_id: str
    """ID of the associated screening."""


class WatchlistScreeningIndividualReviewCreateRequestDict(TypedDict):
    confirmed_hits: list[str]
    dismissed_hits: list[str]
    comment: NotRequired[str | None]
    client_id: NotRequired[str]
    secret: NotRequired[str]
    watchlist_screening_id: str
