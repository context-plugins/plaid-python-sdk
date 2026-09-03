from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .enums.asset_investment_transaction_type import AssetInvestmentTransactionTypeOrStr
from .enums.asset_transaction_category_type import AssetTransactionCategoryTypeOrStr
from .enums.asset_transaction_type import AssetTransactionTypeOrStr


class AssetTransactionDetail(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    asset_transaction_unique_identifier: str = Field(alias="AssetTransactionUniqueIdentifier")
    """A vendor created unique Identifier."""

    asset_transaction_amount: float = Field(alias="AssetTransactionAmount")
    """Asset Transaction Amount."""

    asset_transaction_date: Date = Field(alias="AssetTransactionDate")
    """Asset Transaction Date."""

    asset_transaction_post_date: Date = Field(alias="AssetTransactionPostDate")
    """Asset Transaction Post Date."""

    asset_transaction_type: AssetTransactionTypeOrStr = Field(alias="AssetTransactionType")
    """Asset Transaction Type."""

    asset_investment_transaction_type: OptionalNullable[AssetInvestmentTransactionTypeOrStr] = Field(
        default=UNSET, alias="AssetInvestmentTransactionType"
    )
    """Asset Investment Transaction Type Enumerated derived by Vendor."""

    asset_transaction_paid_by_name: str | None = Field(alias="AssetTransactionPaidByName")
    """Populate with who did the transaction."""

    asset_transaction_paid_to_name: OptionalNullable[str] = Field(default=UNSET, alias="AssetTransactionPaidToName")
    """Populate with for whom the transaction is done"""

    asset_transaction_type_additional_description: str | None = Field(alias="AssetTransactionTypeAdditionalDescription")
    """FI Provided - examples are atm, cash, check, credit, debit, deposit, directDebit, directDeposit, dividend, fee,
    interest, other, payment, pointOfSale, repeatPayment, serviceCharge, transfer."""

    asset_investment_transaction_type_description: str | None = Field(alias="AssetInvestmentTransactionTypeDescription")
    """Asset Investment Transaction Type Description."""

    asset_transaction_category_type: AssetTransactionCategoryTypeOrStr | None = Field(
        alias="AssetTransactionCategoryType"
    )
    """Asset Transaction Category Type Enumerated derived by Vendor."""

    financial_institution_transaction_identifier: str | None = Field(alias="FinancialInstitutionTransactionIdentifier")
    """FI provided Transaction Identifier."""


class AssetTransactionDetailDict(TypedDict):
    asset_transaction_unique_identifier: str
    asset_transaction_amount: float
    asset_transaction_date: Date
    asset_transaction_post_date: Date
    asset_transaction_type: AssetTransactionTypeOrStr
    asset_investment_transaction_type: NotRequired[AssetInvestmentTransactionTypeOrStr | None]
    asset_transaction_paid_by_name: str | None
    asset_transaction_paid_to_name: NotRequired[str | None]
    asset_transaction_type_additional_description: str | None
    asset_investment_transaction_type_description: str | None
    asset_transaction_category_type: AssetTransactionCategoryTypeOrStr | None
    financial_institution_transaction_identifier: str | None
