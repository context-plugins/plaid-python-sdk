from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_asset_transaction import CreditFreddieMacAssetTransaction, CreditFreddieMacAssetTransactionDict


class CreditFreddieMacAssetTransactions(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_transaction: list[CreditFreddieMacAssetTransaction] = Field(alias="ASSET_TRANSACTION")


class CreditFreddieMacAssetTransactionsDict(TypedDict):
    asset_transaction: list[CreditFreddieMacAssetTransaction | CreditFreddieMacAssetTransactionDict]
