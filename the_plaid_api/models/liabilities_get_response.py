from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .item import Item, ItemDict
from .liabilities_object import LiabilitiesObject, LiabilitiesObjectDict


class LiabilitiesGetResponse(SdkBaseModel):
    """LiabilitiesGetResponse defines the response schema for ``/liabilities/get``"""

    accounts: list[Account]
    """An array of accounts associated with the Item"""

    item: Item
    """Metadata about the Item."""

    liabilities: LiabilitiesObject
    """An object containing liability accounts"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class LiabilitiesGetResponseDict(TypedDict):
    accounts: list[AccountDict]
    item: ItemDict
    liabilities: LiabilitiesObjectDict
    request_id: str
