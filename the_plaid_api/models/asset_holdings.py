from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_holding import AssetHolding, AssetHoldingDict


class AssetHoldings(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_holding: list[AssetHolding] = Field(alias="ASSET_HOLDING")


class AssetHoldingsDict(TypedDict):
    asset_holding: list[AssetHolding | AssetHoldingDict]
