from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OauthIntrospectResponse(SdkBaseModel):
    """OAuth token introspect response"""

    active: bool
    """Boolean indicator of whether or not the presented token is currently active. A ``true`` value indicates that the
    token has been issued, has not been revoked, and is within the time window of validity."""

    scope: Optional[str] = UNSET
    """A space-separated list of scopes associated with this token, in the format described in
    https://datatracker.ietf.org/doc/html/rfc6749#section-3.3. Currently accepted values are:

    ``user:read`` allows reading user data. ``user:write`` allows writing user data. ``exchange`` allows exchanging a
    token using the ``urn:plaid:params:oauth:user-token`` subject token type. ``mcp:dashboard`` allows access to the MCP
    dashboard server."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    exp: Optional[int] = UNSET
    """Expiration time as UNIX timestamp since January 1 1970 UTC"""

    iat: Optional[int] = UNSET
    """Issued at time as UNIX timestamp since January 1 1970 UTC"""

    sub: Optional[str] = UNSET
    """Subject of the token"""

    aud: Optional[str] = UNSET
    """Audience of the token"""

    iss: Optional[str] = UNSET
    """Issuer of the token"""

    token_type: Optional[str] = UNSET
    """Type of the token"""

    user_id: Optional[str] = UNSET
    """User ID of the token"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class OauthIntrospectResponseDict(TypedDict):
    active: bool
    scope: NotRequired[str]
    client_id: NotRequired[str]
    exp: NotRequired[int]
    iat: NotRequired[int]
    sub: NotRequired[str]
    aud: NotRequired[str]
    iss: NotRequired[str]
    token_type: NotRequired[str]
    user_id: NotRequired[str]
    request_id: str
