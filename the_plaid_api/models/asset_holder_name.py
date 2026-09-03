from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetHolderName(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    full_name: str = Field(alias="FullName")
    """The unparsed name of either an individual or a legal entity."""


class AssetHolderNameDict(TypedDict):
    full_name: str
