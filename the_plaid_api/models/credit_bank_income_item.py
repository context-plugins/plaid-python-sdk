from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .credit_bank_income_account import CreditBankIncomeAccount, CreditBankIncomeAccountDict
from .credit_bank_income_source import CreditBankIncomeSource, CreditBankIncomeSourceDict


class CreditBankIncomeItem(SdkBaseModel):
    """The details and metadata for an end user's Item."""

    bank_income_accounts: Optional[list[CreditBankIncomeAccount]] = UNSET
    """The Item's accounts that have Bank Income data."""

    bank_income_sources: Optional[list[CreditBankIncomeSource]] = UNSET
    """The income sources for this Item. Each entry in the array is a single income source."""

    last_updated_time: Optional[RFC3339DateTime] = UNSET
    """The time when this Item's data was last retrieved from the financial institution."""

    institution_id: Optional[str] = UNSET
    """The unique identifier of the institution associated with the Item."""

    institution_name: Optional[str] = UNSET
    """The name of the institution associated with the Item."""

    item_id: Optional[str] = UNSET
    """The unique identifier for the Item."""


class CreditBankIncomeItemDict(TypedDict):
    bank_income_accounts: NotRequired[list[CreditBankIncomeAccount | CreditBankIncomeAccountDict]]
    bank_income_sources: NotRequired[list[CreditBankIncomeSource | CreditBankIncomeSourceDict]]
    last_updated_time: NotRequired[RFC3339DateTime]
    institution_id: NotRequired[str]
    institution_name: NotRequired[str]
    item_id: NotRequired[str]
