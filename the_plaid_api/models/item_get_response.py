from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .item_status_nullable import ItemStatusNullable, ItemStatusNullableDict
from .item_with_consent_fields import ItemWithConsentFields, ItemWithConsentFieldsDict


class ItemGetResponse(SdkBaseModel):
    """ItemGetResponse defines the response schema for ``/item/get`` and ``/item/webhook/update``"""

    item: ItemWithConsentFields
    """Metadata about the Item"""

    status: OptionalNullable[ItemStatusNullable] = UNSET
    """An object with information about the status of the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemGetResponseDict(TypedDict):
    item: ItemWithConsentFieldsDict
    status: NotRequired[ItemStatusNullableDict | None]
    request_id: str
