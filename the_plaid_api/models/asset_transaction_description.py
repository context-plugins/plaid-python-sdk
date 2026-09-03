from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetTransactionDescription(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_transaction_description: str = Field(alias="AssetTransactionDescription")
    """Asset Transaction Description String up to 3 occurrences 1 required."""


class AssetTransactionDescriptionDict(TypedDict):
    asset_transaction_description: str
