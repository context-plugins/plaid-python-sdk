from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_assets import CreditFreddieMacAssets, CreditFreddieMacAssetsDict


class CreditFreddieMacVerificationOfAssetResponse(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    assets: CreditFreddieMacAssets = Field(alias="ASSETS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class CreditFreddieMacVerificationOfAssetResponseDict(TypedDict):
    assets: CreditFreddieMacAssets | CreditFreddieMacAssetsDict
