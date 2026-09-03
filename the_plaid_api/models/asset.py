from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_detail import AssetDetail, AssetDetailDict
from .asset_holder import AssetHolder, AssetHolderDict
from .asset_owners import AssetOwners, AssetOwnersDict
from .asset_transactions import AssetTransactions, AssetTransactionsDict
from .validation_sources import ValidationSources, ValidationSourcesDict


class Asset(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_detail: AssetDetail = Field(alias="ASSET_DETAIL")
    """Details about an asset."""

    asset_owners: AssetOwners = Field(alias="ASSET_OWNERS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_holder: AssetHolder = Field(alias="ASSET_HOLDER")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_transactions: AssetTransactions = Field(alias="ASSET_TRANSACTIONS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    validation_sources: ValidationSources = Field(alias="VALIDATION_SOURCES")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class AssetDict(TypedDict):
    asset_detail: AssetDetail | AssetDetailDict
    asset_owners: AssetOwners | AssetOwnersDict
    asset_holder: AssetHolder | AssetHolderDict
    asset_transactions: AssetTransactions | AssetTransactionsDict
    validation_sources: ValidationSources | ValidationSourcesDict
