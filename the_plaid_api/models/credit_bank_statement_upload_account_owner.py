from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_bank_statement_upload_account_owner_address import (
    CreditBankStatementUploadAccountOwnerAddress,
    CreditBankStatementUploadAccountOwnerAddressDict,
)


class CreditBankStatementUploadAccountOwner(SdkBaseModel):
    """An object containing data about the owner of the bank account for the uploaded bank statement."""

    name: str | None
    """The name of the account owner"""

    address: CreditBankStatementUploadAccountOwnerAddress
    """Address on the uploaded bank statement"""


class CreditBankStatementUploadAccountOwnerDict(TypedDict):
    name: str | None
    address: CreditBankStatementUploadAccountOwnerAddress | CreditBankStatementUploadAccountOwnerAddressDict
