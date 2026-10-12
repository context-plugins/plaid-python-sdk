from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .assets import Assets, AssetsDict


class VerificationOfAssetResponse(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    assets: Assets = Field(alias="ASSETS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class VerificationOfAssetResponseDict(TypedDict):
    assets: AssetsDict
