from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.credit_bank_income_account_type import CreditBankIncomeAccountTypeOrStr
from .enums.depository_account_subtype import DepositoryAccountSubtypeOrStr
from .owner import Owner, OwnerDict


class CreditBankIncomeAccount(SdkBaseModel):
    """The Item's bank accounts that have the selected data."""

    account_id: str
    """Plaid's unique identifier for the account."""

    mask: str | None
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    name: str
    """The name of the bank account."""

    official_name: str | None
    """The official name of the bank account."""

    subtype: DepositoryAccountSubtypeOrStr
    """Valid account subtypes for depository accounts. For a list containing descriptions of each subtype, see `Account
    schemas <https://plaid.com/docs/api/accounts/#StandaloneAccountType-depository>`__."""

    type_: CreditBankIncomeAccountTypeOrStr = Field(alias="type")
    """The account type. This will always be ``depository``."""

    owners: list[Owner]
    """Data returned by the financial institution about the account owner or owners. Identity information is optional,
    so field may return an empty array."""


class CreditBankIncomeAccountDict(TypedDict):
    account_id: str
    mask: str | None
    name: str
    official_name: str | None
    subtype: DepositoryAccountSubtypeOrStr
    type_: CreditBankIncomeAccountTypeOrStr
    owners: list[OwnerDict]
