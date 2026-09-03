from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_bank_statement_upload_bank_account import (
    CreditBankStatementUploadBankAccount,
    CreditBankStatementUploadBankAccountDict,
)
from .credit_bank_statement_upload_transaction import (
    CreditBankStatementUploadTransaction,
    CreditBankStatementUploadTransactionDict,
)
from .credit_document_metadata import CreditDocumentMetadata, CreditDocumentMetadataDict


class CreditBankStatementUploadObject(SdkBaseModel):
    """An object containing data that has been parsed from a user-uploaded bank statement."""

    transactions: list[CreditBankStatementUploadTransaction]
    """An array of transactions appearing on the bank statement."""

    document_metadata: CreditDocumentMetadata
    """Object representing metadata pertaining to the document."""

    document_id: str | None
    """An identifier of the document referenced by the document metadata."""

    bank_accounts: list[CreditBankStatementUploadBankAccount]
    """An array of bank accounts associated with the uploaded bank statement."""


class CreditBankStatementUploadObjectDict(TypedDict):
    transactions: list[CreditBankStatementUploadTransaction | CreditBankStatementUploadTransactionDict]
    document_metadata: CreditDocumentMetadata | CreditDocumentMetadataDict
    document_id: str | None
    bank_accounts: list[CreditBankStatementUploadBankAccount | CreditBankStatementUploadBankAccountDict]
