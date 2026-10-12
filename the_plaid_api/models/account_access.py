from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .account_product_access_nullable import AccountProductAccessNullable, AccountProductAccessNullableDict


class AccountAccess(SdkBaseModel):
    """Allow or disallow product access by account. Unlisted (e.g. missing) accounts will be considered
    ``new_accounts``."""

    unique_id: str
    """The unique account identifier for this account. This value must match that returned by the data access API for
    this account."""

    authorized: bool | None = True
    """Allow the application to see this account (and associated details, including balance) in the list of accounts. If
    unset, defaults to ``true``."""

    account_product_access: OptionalNullable[AccountProductAccessNullable] = UNSET
    """Allow the application to access specific products on this account"""


class AccountAccessDict(TypedDict):
    unique_id: str
    authorized: NotRequired[bool | None]
    account_product_access: NotRequired[AccountProductAccessNullableDict | None]
