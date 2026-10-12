from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .credit_amount_with_currency import CreditAmountWithCurrency, CreditAmountWithCurrencyDict
from .credit_bank_income_historical_summary import (
    CreditBankIncomeHistoricalSummary,
    CreditBankIncomeHistoricalSummaryDict,
)


class CreditBankIncomeSummary(SdkBaseModel):
    """Summary for bank income across all income sources and items (max history of 730 days)."""

    total_amount: Optional[float] = UNSET
    """Total amount of earnings across all the income sources in the end user's Items for the days requested by the
    client. This may return an incorrect value if the summary includes income sources in multiple currencies. Please use
    https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts
    instead."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO 4217 currency code of the amount or balance. Please use
    https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts
    instead."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries. Please use
    https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts
    instead."""

    total_amounts: Optional[list[CreditAmountWithCurrency]] = UNSET
    """Total amount of earnings across all the income sources in the end user's Items for the days requested by the
    client. This can contain multiple amounts, with each amount denominated in one unique currency."""

    start_date: Optional[Date] = UNSET
    """The earliest date within the days requested in which all income sources identified by Plaid appear in a user's
    account. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Optional[Date] = UNSET
    """The latest date in which all income sources identified by Plaid appear in the user's account. The date will be
    returned in an ISO 8601 format (YYYY-MM-DD)."""

    income_sources_count: Optional[int] = UNSET
    """Number of income sources per end user."""

    income_categories_count: Optional[int] = UNSET
    """Number of income categories per end user."""

    income_transactions_count: Optional[int] = UNSET
    """Number of income transactions per end user."""

    historical_summary: Optional[list[CreditBankIncomeHistoricalSummary]] = UNSET


class CreditBankIncomeSummaryDict(TypedDict):
    total_amount: NotRequired[float]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    total_amounts: NotRequired[list[CreditAmountWithCurrencyDict]]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    income_sources_count: NotRequired[int]
    income_categories_count: NotRequired[int]
    income_transactions_count: NotRequired[int]
    historical_summary: NotRequired[list[CreditBankIncomeHistoricalSummaryDict]]
