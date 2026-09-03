from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OauthTokenResponse(SdkBaseModel):
    """OAuth token grant success response"""

    access_token: str
    """Access token for OAuth"""

    refresh_token: str
    """Refresh token for OAuth"""

    token_type: str
    """The type of the returned token. ``Bearer`` for OAuth access tokens."""

    expires_in: int
    """Time remaining in seconds before expiration."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class OauthTokenResponseDict(TypedDict):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    request_id: str
