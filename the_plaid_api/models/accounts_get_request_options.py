from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountsGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/accounts/get`` results."""

    account_ids: Optional[list[str]] = UNSET
    """An array of ``account_ids`` to retrieve for the Account."""


class AccountsGetRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
