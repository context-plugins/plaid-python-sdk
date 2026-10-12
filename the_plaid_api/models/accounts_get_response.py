from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .item import Item, ItemDict


class AccountsGetResponse(SdkBaseModel):
    """AccountsGetResponse defines the response schema for ``/accounts/get`` and ``/accounts/balance/get``."""

    accounts: list[Account]
    """An array of financial institution accounts associated with the Item. If ``/accounts/balance/get`` was called,
    each account will include real-time balance information."""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class AccountsGetResponseDict(TypedDict):
    accounts: list[AccountDict]
    item: ItemDict
    request_id: str
