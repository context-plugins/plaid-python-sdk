from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ItemPublicTokenCreateResponse(SdkBaseModel):
    """ItemPublicTokenCreateResponse defines the response schema for ``/item/public_token/create``"""

    public_token: str
    """A ``public_token`` for the particular Item corresponding to the specified ``access_token``"""

    expiration: Optional[RFC3339DateTime] = UNSET
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemPublicTokenCreateResponseDict(TypedDict):
    public_token: str
    expiration: NotRequired[RFC3339DateTime]
    request_id: str
