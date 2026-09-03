from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .session_token_create_response_link import SessionTokenCreateResponseLink, SessionTokenCreateResponseLinkDict


class SessionTokenCreateResponse(SdkBaseModel):
    """SessionTokenCreateResponse defines the response schema for ``/session/token/create``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    link: Optional[SessionTokenCreateResponseLink] = UNSET
    """Response data for ``/session/token/create`` intended for use with the Link SDK."""


class SessionTokenCreateResponseDict(TypedDict):
    request_id: str
    link: NotRequired[SessionTokenCreateResponseLink | SessionTokenCreateResponseLinkDict]
