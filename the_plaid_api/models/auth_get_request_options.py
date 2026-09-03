from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuthGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/auth/get`` results."""

    account_ids: Optional[list[str]] = UNSET
    """A list of ``account_ids`` to retrieve for the Item. Note: An error will be returned if a provided ``account_id``
    is not associated with the Item."""


class AuthGetRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
