from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_identity import AccountIdentity, AccountIdentityDict
from .item import Item, ItemDict


class IdentityGetResponse(SdkBaseModel):
    """IdentityGetResponse defines the response schema for ``/identity/get``"""

    accounts: list[AccountIdentity]
    """The accounts for which Identity data has been requested"""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IdentityGetResponseDict(TypedDict):
    accounts: list[AccountIdentityDict]
    item: ItemDict
    request_id: str
