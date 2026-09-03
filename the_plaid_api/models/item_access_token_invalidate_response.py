from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ItemAccessTokenInvalidateResponse(SdkBaseModel):
    """ItemAccessTokenInvalidateResponse defines the response schema for ``/item/access_token/invalidate``"""

    new_access_token: str
    """The access token associated with the Item for which data is being requested."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemAccessTokenInvalidateResponseDict(TypedDict):
    new_access_token: str
    request_id: str
