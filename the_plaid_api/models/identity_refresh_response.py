from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IdentityRefreshResponse(SdkBaseModel):
    """IdentityRefreshResponse defines the response schema for ``/identity/refresh``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IdentityRefreshResponseDict(TypedDict):
    request_id: str
