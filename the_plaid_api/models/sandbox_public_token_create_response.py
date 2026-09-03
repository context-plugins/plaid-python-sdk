from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxPublicTokenCreateResponse(SdkBaseModel):
    """SandboxPublicTokenCreateResponse defines the response schema for ``/sandbox/public_token/create``"""

    public_token: str
    """A public token that can be exchanged for an access token using ``/item/public_token/exchange``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxPublicTokenCreateResponseDict(TypedDict):
    public_token: str
    request_id: str
