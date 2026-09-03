from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class CreditBankStatementUploadTransaction(SdkBaseModel):
    """An object containing data about a transaction appearing on a user-uploaded bank statement."""

    amount: float | None
    """The value of the transaction. A negative amount indicates that money moved into the account (such as a paycheck
    being deposited)."""

    date: Date | None
    """The date of when the transaction was made, in ISO 8601 format (YYYY-MM-DD)."""

    original_description: str | None
    """The raw description of the transaction as it appears on the bank statement."""

    account_id: str | None
    """The unique id of the bank account that this transaction occurs in"""


class CreditBankStatementUploadTransactionDict(TypedDict):
    amount: float | None
    date: Date | None
    original_description: str | None
    account_id: str | None
