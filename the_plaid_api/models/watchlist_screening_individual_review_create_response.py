from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail, WatchlistScreeningAuditTrailDict


class WatchlistScreeningIndividualReviewCreateResponse(SdkBaseModel):
    """A review submitted by a team member for an individual watchlist screening. A review can be either a comment on
    the current screening state, actions taken against hits attached to the watchlist screening, or both."""

    id: str
    """ID of the associated review."""

    confirmed_hits: list[str]
    """Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once
    confirmed. In most cases, confirmed hits indicate that the customer should be rejected."""

    dismissed_hits: list[str]
    """Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once
    dismissed."""

    comment: str | None
    """A comment submitted by a team member as part of reviewing a watchlist screening."""

    audit_trail: WatchlistScreeningAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it
    occurred."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WatchlistScreeningIndividualReviewCreateResponseDict(TypedDict):
    id: str
    confirmed_hits: list[str]
    dismissed_hits: list[str]
    comment: str | None
    audit_trail: WatchlistScreeningAuditTrailDict
    request_id: str
