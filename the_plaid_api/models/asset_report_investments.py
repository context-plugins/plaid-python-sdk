from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .asset_report_investment_holding import AssetReportInvestmentHolding, AssetReportInvestmentHoldingDict
from .asset_report_investment_security import AssetReportInvestmentSecurity, AssetReportInvestmentSecurityDict
from .asset_report_investment_transaction import AssetReportInvestmentTransaction, AssetReportInvestmentTransactionDict


class AssetReportInvestments(SdkBaseModel):
    """A set of fields describing the investments data on an account."""

    holdings: Optional[list[AssetReportInvestmentHolding]] = UNSET
    """Quantities and values of securities held in the investment account. Map to the ``securities`` array for security
    details."""

    securities: Optional[list[AssetReportInvestmentSecurity]] = UNSET
    """Details of specific securities held in on the investment account."""

    transactions: Optional[list[AssetReportInvestmentTransaction]] = UNSET
    """Transaction history on the investment account."""


class AssetReportInvestmentsDict(TypedDict):
    holdings: NotRequired[list[AssetReportInvestmentHoldingDict]]
    securities: NotRequired[list[AssetReportInvestmentSecurityDict]]
    transactions: NotRequired[list[AssetReportInvestmentTransactionDict]]
