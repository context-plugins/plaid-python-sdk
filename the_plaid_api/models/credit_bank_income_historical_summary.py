from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .credit_amount_with_currency import CreditAmountWithCurrency, CreditAmountWithCurrencyDict
from .credit_bank_income_transaction import CreditBankIncomeTransaction, CreditBankIncomeTransactionDict


class CreditBankIncomeHistoricalSummary(SdkBaseModel):
    """The end user's monthly summary for the income source(s)."""

    total_amount: Optional[float] = UNSET
    """Total amount of earnings for the income source(s) of the user for the month in the summary. This may return an
    incorrect value if the summary includes income sources in multiple currencies. Please use
    https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts
    instead."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO 4217 currency code of the amount or balance. Please use
    https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts
    instead."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries. Please use
    https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts
    instead."""

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

    transactions: Optional[list[CreditBankIncomeTransaction]] = UNSET


class CreditBankIncomeHistoricalSummaryDict(TypedDict):
    total_amount: NotRequired[float]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    total_amounts: NotRequired[list[CreditAmountWithCurrencyDict]]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    transactions: NotRequired[list[CreditBankIncomeTransactionDict]]
