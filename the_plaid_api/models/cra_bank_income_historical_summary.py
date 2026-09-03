from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .cra_bank_income_transaction import CraBankIncomeTransaction, CraBankIncomeTransactionDict
from .credit_amount_with_currency import CreditAmountWithCurrency, CreditAmountWithCurrencyDict


class CraBankIncomeHistoricalSummary(SdkBaseModel):
    """The end user's monthly summary for the income source(s)."""

    total_amounts: Optional[list[CreditAmountWithCurrency]] = UNSET
    """Total amount of earnings for the income source(s) of the user for the month in the summary. This can contain
    multiple amounts, with each amount denominated in one unique currency."""

    start_date: Optional[Date] = UNSET
    """The start date of the period covered in this monthly summary. This date will be the first day of the month,
    unless the month being covered is a partial month because it is the first month included in the summary and the date
    range being requested does not begin with the first day of the month. The date will be returned in an ISO 8601
    format (YYYY-MM-DD)."""

    end_date: Optional[Date] = UNSET
    """The end date of the period included in this monthly summary. This date will be the last day of the month, unless
    the month being covered is a partial month because it is the last month included in the summary and the date range
    being requested does not end with the last day of the month. The date will be returned in an ISO 8601 format
    (YYYY-MM-DD)."""

    transactions: Optional[list[CraBankIncomeTransaction]] = UNSET


class CraBankIncomeHistoricalSummaryDict(TypedDict):
    total_amounts: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    transactions: NotRequired[list[CraBankIncomeTransaction | CraBankIncomeTransactionDict]]
