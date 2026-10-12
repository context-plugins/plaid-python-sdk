from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .account_assets import AccountAssets, AccountAssetsDict


class AssetReportItem(SdkBaseModel):
    """A representation of an Item within an Asset Report."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    institution_name: str
    """The full financial institution name associated with the Item."""

    institution_id: str
    """The id of the financial institution associated with the Item."""

    date_last_updated: RFC3339DateTime
    """The date and time when this Item's data was last retrieved from the financial institution, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    accounts: list[AccountAssets]
    """Data about each of the accounts open on the Item."""


class AssetReportItemDict(TypedDict):
    item_id: str
    institution_name: str
    institution_id: str
    date_last_updated: RFC3339DateTime
    accounts: list[AccountAssetsDict]
