from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .watchlist_screening_request_search_terms import (
    WatchlistScreeningRequestSearchTerms,
    WatchlistScreeningRequestSearchTermsDict,
)


class WatchlistScreeningIndividualCreateRequest(SdkBaseModel):
    """Request input for creating an individual watchlist screening"""

    search_terms: WatchlistScreeningRequestSearchTerms
    """Search inputs for creating a watchlist screening"""

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


class WatchlistScreeningIndividualCreateRequestDict(TypedDict):
    search_terms: WatchlistScreeningRequestSearchTerms | WatchlistScreeningRequestSearchTermsDict
    client_user_id: NotRequired[str]
    client_id: NotRequired[str]
    secret: NotRequired[str]
