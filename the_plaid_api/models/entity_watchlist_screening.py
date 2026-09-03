from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .entity_watchlist_screening_search_terms import (
    EntityWatchlistScreeningSearchTerms,
    EntityWatchlistScreeningSearchTermsDict,
)
from .enums.watchlist_screening_status import WatchlistScreeningStatusOrStr
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail, WatchlistScreeningAuditTrailDict


class EntityWatchlistScreening(SdkBaseModel):
    """The entity screening object allows you to represent an entity in your system, update its profile, and search for
    it on various watchlists. Note: Rejected entity screenings will not receive new hits, regardless of entity program
    configuration."""

    id: str
    """ID of the associated entity screening."""

    search_terms: EntityWatchlistScreeningSearchTerms
    """Search terms associated with an entity used for searching against watchlists"""

    assignee: str | None
    """ID of the associated user. To retrieve the email address or other details of the person corresponding to this ID,
    use ``/dashboard_user/get``."""

    status: WatchlistScreeningStatusOrStr
    """A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""

    client_user_id: str | None
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    audit_trail: WatchlistScreeningAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it
    occurred."""


class EntityWatchlistScreeningDict(TypedDict):
    id: str
    search_terms: EntityWatchlistScreeningSearchTerms | EntityWatchlistScreeningSearchTermsDict
    assignee: str | None
    status: WatchlistScreeningStatusOrStr
    client_user_id: str | None
    audit_trail: WatchlistScreeningAuditTrail | WatchlistScreeningAuditTrailDict
