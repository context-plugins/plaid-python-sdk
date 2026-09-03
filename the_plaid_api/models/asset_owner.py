from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetOwner(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_owner_text: str | None = Field(alias="AssetOwnerText")
    """Account Owner Full Name."""


class AssetOwnerDict(TypedDict):
    asset_owner_text: str | None
