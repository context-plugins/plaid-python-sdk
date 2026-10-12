from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .credit_bank_statement_upload_object import CreditBankStatementUploadObject, CreditBankStatementUploadObjectDict
from .payroll_item_status import PayrollItemStatus, PayrollItemStatusDict


class CreditBankStatementUploadItem(SdkBaseModel):
    """An object containing information about the bank statement upload Item."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    bank_statements: list[CreditBankStatementUploadObject]
    status: PayrollItemStatus | None
    """Details about the status of the payroll item."""

    updated_at: RFC3339DateTime | None
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DDTHH:mm:ssZ) indicating the last
    time that the Item was updated."""


class CreditBankStatementUploadItemDict(TypedDict):
    item_id: str
    bank_statements: list[CreditBankStatementUploadObjectDict]
    status: PayrollItemStatusDict | None
    updated_at: RFC3339DateTime | None
