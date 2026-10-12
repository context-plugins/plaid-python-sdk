from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .link_token_get_metadata_response import LinkTokenGetMetadataResponse, LinkTokenGetMetadataResponseDict
from .link_token_get_sessions_response import LinkTokenGetSessionsResponse, LinkTokenGetSessionsResponseDict


class LinkTokenGetResponse(SdkBaseModel):
    """LinkTokenGetResponse defines the response schema for ``/link/token/get``"""

    link_token: str
    """A ``link_token``, which can be supplied to Link in order to initialize it and receive a ``public_token``, which
    can be exchanged for an ``access_token``."""

    created_at: RFC3339DateTime | None
    """The creation timestamp for the ``link_token``, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    expiration: RFC3339DateTime | None
    """The expiration timestamp for the ``link_token``, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    link_sessions: Optional[list[LinkTokenGetSessionsResponse]] = UNSET
    """Information about Link sessions created using this ``link_token``. Session data will be provided for up to six
    hours after the session has ended."""

    metadata: LinkTokenGetMetadataResponse
    """An object specifying the arguments originally provided to the ``/link/token/create`` call."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class LinkTokenGetResponseDict(TypedDict):
    link_token: str
    created_at: RFC3339DateTime | None
    expiration: RFC3339DateTime | None
    link_sessions: NotRequired[list[LinkTokenGetSessionsResponseDict]]
    metadata: LinkTokenGetMetadataResponseDict
    user_id: NotRequired[str]
    request_id: str
