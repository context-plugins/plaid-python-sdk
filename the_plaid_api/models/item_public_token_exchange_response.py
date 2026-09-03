from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ItemPublicTokenExchangeResponse(SdkBaseModel):
    """ItemPublicTokenExchangeResponse defines the response schema for ``/item/public_token/exchange``"""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    item_id: str
    """The ``item_id`` value of the Item associated with the returned ``access_token``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemPublicTokenExchangeResponseDict(TypedDict):
    access_token: str
    item_id: str
    request_id: str
