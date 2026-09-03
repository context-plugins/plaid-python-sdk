from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_owner import AssetOwner, AssetOwnerDict


class AssetOwners(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_owner: list[AssetOwner] = Field(alias="ASSET_OWNER")
    """A list of up to 4 account owners' full names."""


class AssetOwnersDict(TypedDict):
    asset_owner: list[AssetOwner | AssetOwnerDict]
