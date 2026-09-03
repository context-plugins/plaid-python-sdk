from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OauthRevokeResponse(SdkBaseModel):
    """Successful OAuth token revoke response"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class OauthRevokeResponseDict(TypedDict):
    request_id: str
