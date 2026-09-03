from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvestmentHoldingsGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/investments/holdings/get`` results. If provided, must not be ``null``."""

    account_ids: Optional[list[str]] = UNSET
    """An array of ``account_id``s to retrieve for the Item. An error will be returned if a provided ``account_id`` is
    not associated with the Item."""


class InvestmentHoldingsGetRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
