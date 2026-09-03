from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.asset_holding_restricted_indicator import AssetHoldingRestrictedIndicatorOrStr
from .enums.asset_holding_type import AssetHoldingTypeOrStr


class AssetHolding(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_holding_id: str | None = Field(alias="AssetHoldingID")
    """Unique id of investment position"""

    currency: str | None = Field(alias="Currency")
    """US Dollar"""

    asset_holding_description: str | None = Field(alias="AssetHoldingDescription")
    """Description of holding"""

    asset_holding_symbol: str | None = Field(alias="AssetHoldingSymbol")
    """Investment position's market ticker symbol"""

    asset_holding_security_name: str | None = Field(alias="AssetHoldingSecurityName")
    """Security name of investment holding"""

    asset_holding_units: float | None = Field(alias="AssetHoldingUnits")
    """Number of units of holding"""

    asset_holding_market_value_amount: float | None = Field(alias="AssetHoldingMarketValueAmount")
    """market value of investment position"""

    asset_holding_current_price_amount: float | None = Field(alias="AssetHoldingCurrentPriceAmount")
    """current price of investment holding"""

    asset_holding_type: AssetHoldingTypeOrStr | None = Field(alias="AssetHoldingType")
    """Type of holding (e.g. bond, stock, crypto, other)"""

    asset_holding_restricted_indicator: AssetHoldingRestrictedIndicatorOrStr | None = Field(
        alias="AssetHoldingRestrictedIndicator"
    )
    """Whether or not the stock is restricted, i.e. "Restricted" or "Not Restricted"
    """

    asset_holding_vested_amount: float | None = Field(alias="AssetHoldingVestedAmount")
    """Amount of holding vested"""


class AssetHoldingDict(TypedDict):
    asset_holding_id: str | None
    currency: str | None
    asset_holding_description: str | None
    asset_holding_symbol: str | None
    asset_holding_security_name: str | None
    asset_holding_units: float | None
    asset_holding_market_value_amount: float | None
    asset_holding_current_price_amount: float | None
    asset_holding_type: AssetHoldingTypeOrStr | None
    asset_holding_restricted_indicator: AssetHoldingRestrictedIndicatorOrStr | None
    asset_holding_vested_amount: float | None
