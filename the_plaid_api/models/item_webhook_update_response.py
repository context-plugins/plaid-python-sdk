from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .item import Item, ItemDict


class ItemWebhookUpdateResponse(SdkBaseModel):
    """ItemWebhookUpdateResponse defines the response schema for ``/item/webhook/update``"""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemWebhookUpdateResponseDict(TypedDict):
    item: ItemDict
    request_id: str
