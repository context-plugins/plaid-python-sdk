from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .item import Item, ItemDict


class UserItemsGetResponse(SdkBaseModel):
    """UserItemsGetResponse defines the response schema for ``/user/items/get``"""

    items: list[Item]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class UserItemsGetResponseDict(TypedDict):
    items: list[ItemDict]
    request_id: str
