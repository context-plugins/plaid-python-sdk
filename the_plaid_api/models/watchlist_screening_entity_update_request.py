from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.watchlist_screening_entity_update_request_resettable_field import (
    WatchlistScreeningEntityUpdateRequestResettableFieldOrStr,
)
from .enums.watchlist_screening_status import WatchlistScreeningStatusOrStr
from .update_entity_screening_request_search_terms import (
    UpdateEntityScreeningRequestSearchTerms,
    UpdateEntityScreeningRequestSearchTermsDict,
)


class WatchlistScreeningEntityUpdateRequest(SdkBaseModel):
    """Request input for editing an entity watchlist screening"""

    entity_watchlist_screening_id: str
    """ID of the associated entity screening."""

    search_terms: OptionalNullable[UpdateEntityScreeningRequestSearchTerms] = UNSET
    """Search terms for editing an entity watchlist screening"""

    assignee: Optional[str] = UNSET
    """ID of the associated user. To retrieve the email address or other details of the person corresponding to this ID,
    use ``/dashboard_user/get``."""

    status: Optional[WatchlistScreeningStatusOrStr] = UNSET
    """A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""

    client_user_id: Optional[str] = UNSET
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    reset_fields: OptionalNullable[list[WatchlistScreeningEntityUpdateRequestResettableFieldOrStr]] = UNSET
    """A list of fields to reset back to null"""


class WatchlistScreeningEntityUpdateRequestDict(TypedDict):
    entity_watchlist_screening_id: str
    search_terms: NotRequired[UpdateEntityScreeningRequestSearchTermsDict | None]
    assignee: NotRequired[str]
    status: NotRequired[WatchlistScreeningStatusOrStr]
    client_user_id: NotRequired[str]
    client_id: NotRequired[str]
    secret: NotRequired[str]
    reset_fields: NotRequired[list[WatchlistScreeningEntityUpdateRequestResettableFieldOrStr] | None]
