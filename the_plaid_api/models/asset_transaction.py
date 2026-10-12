from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_transaction_description import AssetTransactionDescription, AssetTransactionDescriptionDict
from .asset_transaction_detail import AssetTransactionDetail, AssetTransactionDetailDict


class AssetTransaction(SdkBaseModel):
    """An object representing..."""

    asset_transaction_detail: AssetTransactionDetail = Field(alias="ASSET_TRANSACTION_DETAIL")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_transaction_descripton: list[AssetTransactionDescription] = Field(alias="ASSET_TRANSACTION_DESCRIPTON")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac. Note that "DESCRIPTON" is an
    intentional misspelling matching the upstream MISMO field name."""


class AssetTransactionDict(TypedDict):
    asset_transaction_detail: AssetTransactionDetailDict
    asset_transaction_descripton: list[AssetTransactionDescriptionDict]
