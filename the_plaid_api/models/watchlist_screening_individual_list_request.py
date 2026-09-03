from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.watchlist_screening_status import WatchlistScreeningStatusOrStr


class WatchlistScreeningIndividualListRequest(SdkBaseModel):
    """Request input for listing watchlist screenings for individuals"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    watchlist_program_id: str
    """ID of the associated program."""

    client_user_id: Optional[str] = UNSET
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    status: Optional[WatchlistScreeningStatusOrStr] = UNSET
    """A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""

    assignee: Optional[str] = UNSET
    """ID of the associated user. To retrieve the email address or other details of the person corresponding to this ID,
    use ``/dashboard_user/get``."""

    cursor: OptionalNullable[str] = UNSET
    """An identifier that determines which page of results you receive."""


class WatchlistScreeningIndividualListRequestDict(TypedDict):
    secret: NotRequired[str]
    client_id: NotRequired[str]
    watchlist_program_id: str
    client_user_id: NotRequired[str]
    status: NotRequired[WatchlistScreeningStatusOrStr]
    assignee: NotRequired[str]
    cursor: NotRequired[str | None]
