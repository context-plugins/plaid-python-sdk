from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_access import AccountAccess, AccountAccessDict
from .product_access import ProductAccess, ProductAccessDict


class ScopesNullable(SdkBaseModel):
    """The scopes object"""

    product_access: Optional[ProductAccess] = UNSET
    """The product access being requested. Used to allow or disallow product access across all accounts. If unset,
    defaults to all products allowed."""

    accounts: Optional[list[AccountAccess]] = UNSET
    new_accounts: bool | None = True
    """Allow access to newly opened accounts as they are opened. If unset, defaults to ``true``."""


class ScopesNullableDict(TypedDict):
    product_access: NotRequired[ProductAccessDict]
    accounts: NotRequired[list[AccountAccessDict]]
    new_accounts: NotRequired[bool | None]
