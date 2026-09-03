from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_transaction import AssetTransaction, AssetTransactionDict


class AssetTransactions(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_transaction: list[AssetTransaction] = Field(alias="ASSET_TRANSACTION")


class AssetTransactionsDict(TypedDict):
    asset_transaction: list[AssetTransaction | AssetTransactionDict]
