from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset import Asset, AssetDict


class Assets(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset: list[Asset] = Field(alias="ASSET")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class AssetsDict(TypedDict):
    asset: list[Asset | AssetDict]
