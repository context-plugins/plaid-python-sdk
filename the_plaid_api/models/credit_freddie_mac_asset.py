from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .asset_detail import AssetDetail, AssetDetailDict
from .asset_holder import AssetHolder, AssetHolderDict
from .asset_holdings import AssetHoldings, AssetHoldingsDict
from .asset_owners import AssetOwners, AssetOwnersDict
from .credit_freddie_mac_asset_transactions import (
    CreditFreddieMacAssetTransactions,
    CreditFreddieMacAssetTransactionsDict,
)
from .validation_sources import ValidationSources, ValidationSourcesDict


class CreditFreddieMacAsset(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_detail: AssetDetail = Field(alias="ASSET_DETAIL")
    """Details about an asset."""

    asset_owners: AssetOwners = Field(alias="ASSET_OWNERS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_holder: AssetHolder = Field(alias="ASSET_HOLDER")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_holdings: Optional[AssetHoldings] = Field(default=UNSET, alias="ASSET_HOLDINGS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_transactions: CreditFreddieMacAssetTransactions = Field(alias="ASSET_TRANSACTIONS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    validation_sources: ValidationSources = Field(alias="VALIDATION_SOURCES")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class CreditFreddieMacAssetDict(TypedDict):
    asset_detail: AssetDetailDict
    asset_owners: AssetOwnersDict
    asset_holder: AssetHolderDict
    asset_holdings: NotRequired[AssetHoldingsDict]
    asset_transactions: CreditFreddieMacAssetTransactionsDict
    validation_sources: ValidationSourcesDict
