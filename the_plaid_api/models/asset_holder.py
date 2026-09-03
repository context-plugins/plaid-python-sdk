from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_holder_name import AssetHolderName, AssetHolderNameDict


class AssetHolder(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    name: AssetHolderName = Field(alias="NAME")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class AssetHolderDict(TypedDict):
    name: AssetHolderName | AssetHolderNameDict
