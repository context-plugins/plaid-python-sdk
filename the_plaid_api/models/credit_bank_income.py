from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .credit_bank_income_item import CreditBankIncomeItem, CreditBankIncomeItemDict
from .credit_bank_income_summary import CreditBankIncomeSummary, CreditBankIncomeSummaryDict
from .credit_bank_income_warning import CreditBankIncomeWarning, CreditBankIncomeWarningDict


class CreditBankIncome(SdkBaseModel):
    """The report of the Bank Income data for an end user."""

    bank_income_id: Optional[str] = UNSET
    """The unique identifier associated with the Bank Income Report."""

    generated_time: Optional[RFC3339DateTime] = UNSET
    """The time when the report was generated."""

    days_requested: Optional[int] = UNSET
    """The number of days requested by the customer for the report."""

    items: Optional[list[CreditBankIncomeItem]] = UNSET
    """The list of Items in the report along with the associated metadata about the Item."""

    bank_income_summary: Optional[CreditBankIncomeSummary] = UNSET
    """Summary for bank income across all income sources and items (max history of 730 days)."""

    warnings: Optional[list[CreditBankIncomeWarning]] = UNSET
    """If data from the report was unable to be retrieved, the warnings will contain information about the error that
    caused the data to be incomplete."""


class CreditBankIncomeDict(TypedDict):
    bank_income_id: NotRequired[str]
    generated_time: NotRequired[RFC3339DateTime]
    days_requested: NotRequired[int]
    items: NotRequired[list[CreditBankIncomeItemDict]]
    bank_income_summary: NotRequired[CreditBankIncomeSummaryDict]
    warnings: NotRequired[list[CreditBankIncomeWarningDict]]
