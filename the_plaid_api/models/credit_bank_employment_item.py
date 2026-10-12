from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .credit_bank_employment import CreditBankEmployment, CreditBankEmploymentDict
from .credit_bank_income_account import CreditBankIncomeAccount, CreditBankIncomeAccountDict


class CreditBankEmploymentItem(SdkBaseModel):
    """The details and metadata for an end user's Item."""

    item_id: str
    """The unique identifier for the Item."""

    last_updated_time: RFC3339DateTime
    """The time when this Item's data was last retrieved from the financial institution, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (e.g. "2018-04-12T03:32:11Z")."""

    institution_id: str
    """The unique identifier of the institution associated with the Item."""

    institution_name: str
    """The name of the institution associated with the Item."""

    bank_employments: list[CreditBankEmployment]
    """The bank employment information for this Item. Each entry in the array is a different employer found."""

    bank_employment_accounts: list[CreditBankIncomeAccount]
    """The Item's accounts that have Bank Employment data."""


class CreditBankEmploymentItemDict(TypedDict):
    item_id: str
    last_updated_time: RFC3339DateTime
    institution_id: str
    institution_name: str
    bank_employments: list[CreditBankEmploymentDict]
    bank_employment_accounts: list[CreditBankIncomeAccountDict]
