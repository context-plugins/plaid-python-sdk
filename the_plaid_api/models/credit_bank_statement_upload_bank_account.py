from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_bank_statement_upload_account_owner import (
    CreditBankStatementUploadAccountOwner,
    CreditBankStatementUploadAccountOwnerDict,
)
from .credit_bank_statement_upload_bank_account_period import (
    CreditBankStatementUploadBankAccountPeriod,
    CreditBankStatementUploadBankAccountPeriodDict,
)


class CreditBankStatementUploadBankAccount(SdkBaseModel):
    """An object containing data about a user's bank account related to an uploaded bank statement."""

    name: str | None
    """The name of the bank account"""

    bank_name: str | None
    """The name of the bank institution."""

    account_type: str | None
    """The type of the bank account."""

    account_number: str | None
    """The bank account number."""

    owner: CreditBankStatementUploadAccountOwner
    """An object containing data about the owner of the bank account for the uploaded bank statement."""

    periods: list[CreditBankStatementUploadBankAccountPeriod]
    """An array of period objects, containing more data on the overall period of the statement."""

    account_id: str | None
    """The unique id of the bank account"""


class CreditBankStatementUploadBankAccountDict(TypedDict):
    name: str | None
    bank_name: str | None
    account_type: str | None
    account_number: str | None
    owner: CreditBankStatementUploadAccountOwner | CreditBankStatementUploadAccountOwnerDict
    periods: list[CreditBankStatementUploadBankAccountPeriod | CreditBankStatementUploadBankAccountPeriodDict]
    account_id: str | None
