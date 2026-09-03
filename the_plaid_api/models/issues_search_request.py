from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IssuesSearchRequest(SdkBaseModel):
    """IssuesSearchRequest defines the request schema for ``/issues/search``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    item_id: Optional[str] = UNSET
    """A unique identifier for the Plaid Item."""

    link_session_id: Optional[str] = UNSET
    """A unique identifier for the Link session."""

    link_session_request_id: Optional[str] = UNSET
    """The ``request_id`` for the Link session that might have had an institution connection issue."""


class IssuesSearchRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    item_id: NotRequired[str]
    link_session_id: NotRequired[str]
    link_session_request_id: NotRequired[str]
