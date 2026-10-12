from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_bank_statement_upload_item import CreditBankStatementUploadItem, CreditBankStatementUploadItemDict


class CreditBankStatementsUploadsGetResponse(SdkBaseModel):
    """CreditBankStatementsUploadsGetResponse defines the response schema for ``/credit/bank_statements/uploads/get``"""

    items: list[CreditBankStatementUploadItem]
    """Array of bank statement upload items."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditBankStatementsUploadsGetResponseDict(TypedDict):
    items: list[CreditBankStatementUploadItemDict]
    request_id: str
