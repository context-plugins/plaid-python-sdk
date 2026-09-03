from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenInvestments(SdkBaseModel):
    """Configuration parameters for the Investments product"""

    allow_unverified_crypto_wallets: Optional[bool] = UNSET
    """If ``true``, allow self-custody crypto wallets to be added without requiring signature verification. Defaults to
    ``false``."""

    allow_manual_entry: Optional[bool] = UNSET
    """If ``true``, allow users to manually enter Investments account and holdings information. Defaults to
    ``false``."""


class LinkTokenInvestmentsDict(TypedDict):
    allow_unverified_crypto_wallets: NotRequired[bool]
    allow_manual_entry: NotRequired[bool]
