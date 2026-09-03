from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LiabilitiesGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/liabilities/get`` results. If provided, ``options`` cannot be null."""

    account_ids: Optional[list[str]] = UNSET
    """A list of accounts to retrieve for the Item.

    An error will be returned if a provided ``account_id`` is not associated with the Item"""


class LiabilitiesGetRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
