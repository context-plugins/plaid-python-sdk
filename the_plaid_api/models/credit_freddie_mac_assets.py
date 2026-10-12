from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_asset import CreditFreddieMacAsset, CreditFreddieMacAssetDict


class CreditFreddieMacAssets(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset: list[CreditFreddieMacAsset] = Field(alias="ASSET")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class CreditFreddieMacAssetsDict(TypedDict):
    asset: list[CreditFreddieMacAssetDict]
