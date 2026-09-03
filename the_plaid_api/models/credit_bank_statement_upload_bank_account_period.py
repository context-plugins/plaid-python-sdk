from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class CreditBankStatementUploadBankAccountPeriod(SdkBaseModel):
    """An object containing data on the overall period of the statement."""

    start_date: Date | None
    """The start date of the statement period in ISO 8601 format (YYYY-MM-DD)."""

    end_date: Date | None
    """The end date of the statement period in ISO 8601 format (YYYY-MM-DD)."""

    starting_balance: float | None
    """The starting balance of the bank account for the period."""

    ending_balance: float | None
    """The ending balance of the bank account for the period."""


class CreditBankStatementUploadBankAccountPeriodDict(TypedDict):
    start_date: Date | None
    end_date: Date | None
    starting_balance: float | None
    ending_balance: float | None
