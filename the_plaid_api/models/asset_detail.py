from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.asset_employer_sponsored_indicator import AssetEmployerSponsoredIndicatorOrStr
from .enums.asset_retirement_indicator import AssetRetirementIndicatorOrStr
from .enums.asset_type import AssetTypeOrStr


class AssetDetail(SdkBaseModel):
    """Details about an asset."""

    asset_unique_identifier: str = Field(alias="AssetUniqueIdentifier")
    """A vendor created unique Identifier."""

    asset_account_identifier: str = Field(alias="AssetAccountIdentifier")
    """A unique alphanumeric string identifying an asset."""

    asset_as_of_date: str = Field(alias="AssetAsOfDate")
    """Account Report As of Date / Create Date. Format YYYY-MM-DD"""

    asset_description: str | None = Field(alias="AssetDescription")
    """A text description that further defines the Asset. This could be used to describe the shares associated with the
    stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an
    asset."""

    asset_available_balance_amount: float = Field(alias="AssetAvailableBalanceAmount")
    """Asset Account Available Balance."""

    asset_current_balance_amount: float = Field(alias="AssetCurrentBalanceAmount")
    """Asset Account Current Balance."""

    asset_holding_balance_amount: OptionalNullable[float] = Field(default=UNSET, alias="AssetHoldingBalanceAmount")
    """Total market value of holdings (non-restricted, vested, not crypto, not other, not cash) Note: Any employer stock
    plan balance must be excluded from the total account balance (identification is 'stock plan')"""

    asset_holding_balance_net_margin_amount: OptionalNullable[float] = Field(
        default=UNSET, alias="AssetHoldingBalanceNetMarginAmount"
    )
    """HoldingsBalance net MarginAmount"""

    asset_bonds_balance_amount: OptionalNullable[float] = Field(default=UNSET, alias="AssetBondsBalanceAmount")
    """Total market value of all bonds held (non-restricted, vested)"""

    asset_stocks_balance_amount: OptionalNullable[float] = Field(default=UNSET, alias="AssetStocksBalanceAmount")
    """Total market value of all stocks held (non-restricted, vested, not employer sponsored stock plan)"""

    asset_crypto_balance_amount: OptionalNullable[float] = Field(default=UNSET, alias="AssetCryptoBalanceAmount")
    """Total balance of all cryptocurrency held (non-restricted, vested)"""

    asset_other_balance_amount: OptionalNullable[float] = Field(default=UNSET, alias="AssetOtherBalanceAmount")
    """Total balance of all other holding types (non-restricted, vested)"""

    asset_margin_amount_balance: OptionalNullable[float] = Field(default=UNSET, alias="AssetMarginAmountBalance")
    """loan balance (amount owed by account owner)"""

    asset_available_cash_balance_amount: OptionalNullable[float] = Field(
        default=UNSET, alias="AssetAvailableCashBalanceAmount"
    )
    """amount available for cash withdrawal"""

    asset_cash_balance_amount: OptionalNullable[float] = Field(default=UNSET, alias="AssetCashBalanceAmount")
    """cash balance of the account"""

    asset_type: AssetTypeOrStr = Field(alias="AssetType")
    """A value from a MISMO prescribed list that specifies financial assets in a mortgage loan transaction. Assets may
    be either liquid or fixed and are associated with a corresponding asset amount."""

    asset_type_additional_description: str | None = Field(alias="AssetTypeAdditionalDescription")
    """Additional Asset Description. Some examples are Investment Tax-Deferred, Loan, 401K, 403B, Checking, Money
    Market, Credit Card, ROTH, 529, Biller, ROLLOVER, CD, Savings, Investment Taxable, IRA, Mortgage, Line Of Credit."""

    asset_days_requested_count: int = Field(alias="AssetDaysRequestedCount")
    """The number of days requested from the Financial Institution. Example: When looking for 3 months of data from the
    FI, pass in 90 days."""

    asset_ownership_type: str | None = Field(alias="AssetOwnershipType")
    """Ownership type of the asset account."""

    asset_retirement_indicator: OptionalNullable[AssetRetirementIndicatorOrStr] = Field(
        default=UNSET, alias="AssetRetirementIndicator"
    )
    """Whether or not the account is a retirement account (e.g., 401K, 403b, 457, thrift savings plans, traditional and
    Roth, IRAs, SEP-IRA, SIMPLE-IRA, KEOGH, state retirement savings plans, other independent and IRS-qualified employer
    retirement plans)"""

    asset_employer_sponsored_indicator: OptionalNullable[AssetEmployerSponsoredIndicatorOrStr] = Field(
        default=UNSET, alias="AssetEmployerSponsoredIndicator"
    )
    """Whether the account is employer sponsored retirement account or not (e.g., 401K, 403b, 457, thrift savings
    plan)"""


class AssetDetailDict(TypedDict):
    asset_unique_identifier: str
    asset_account_identifier: str
    asset_as_of_date: str
    asset_description: str | None
    asset_available_balance_amount: float
    asset_current_balance_amount: float
    asset_holding_balance_amount: NotRequired[float | None]
    asset_holding_balance_net_margin_amount: NotRequired[float | None]
    asset_bonds_balance_amount: NotRequired[float | None]
    asset_stocks_balance_amount: NotRequired[float | None]
    asset_crypto_balance_amount: NotRequired[float | None]
    asset_other_balance_amount: NotRequired[float | None]
    asset_margin_amount_balance: NotRequired[float | None]
    asset_available_cash_balance_amount: NotRequired[float | None]
    asset_cash_balance_amount: NotRequired[float | None]
    asset_type: AssetTypeOrStr
    asset_type_additional_description: str | None
    asset_days_requested_count: int
    asset_ownership_type: str | None
    asset_retirement_indicator: NotRequired[AssetRetirementIndicatorOrStr | None]
    asset_employer_sponsored_indicator: NotRequired[AssetEmployerSponsoredIndicatorOrStr | None]
