from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IncomeVerificationCreateRequestOptions(SdkBaseModel):
    """Optional arguments for ``/income/verification/create``"""

    access_tokens: Optional[list[str]] = UNSET
    """An array of access tokens corresponding to the Items that will be cross-referenced with the product data. Plaid
    will attempt to correlate transaction history from these Items with data from the user's paystub, such as date and
    amount. If the ``transactions`` product was not initialized for the Items during Link, it will be initialized after
    this Link session."""


class IncomeVerificationCreateRequestOptionsDict(TypedDict):
    access_tokens: NotRequired[list[str]]
