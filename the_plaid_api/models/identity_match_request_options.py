from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IdentityMatchRequestOptions(SdkBaseModel):
    """An optional object to filter ``/identity/match`` results"""

    account_ids: Optional[list[str]] = UNSET
    """An array of ``account_ids`` to perform fuzzy match"""


class IdentityMatchRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
