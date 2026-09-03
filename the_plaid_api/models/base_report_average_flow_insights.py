from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .credit_amount_with_currency import CreditAmountWithCurrency, CreditAmountWithCurrencyDict


class BaseReportAverageFlowInsights(SdkBaseModel):
    """Average dollar amount of credit or debit transactions out of the account. This field will only be included for
    depository accounts."""

    start_date: Date
    """The start date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Date
    """The end date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    total_amount: CreditAmountWithCurrency
    """This contains an amount, denominated in the currency specified by either ``iso_currency_code`` or
    ``unofficial_currency_code``"""


class BaseReportAverageFlowInsightsDict(TypedDict):
    start_date: Date
    end_date: Date
    total_amount: CreditAmountWithCurrency | CreditAmountWithCurrencyDict
