from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_amount_with_currency import CreditAmountWithCurrency, CreditAmountWithCurrencyDict


class BaseReportAverageMonthlyBalances(SdkBaseModel):
    """Average balance in dollar amount per month"""

    start_date: str
    """The start date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: str
    """The end date of this time period. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    average_balance: CreditAmountWithCurrency
    """This contains an amount, denominated in the currency specified by either ``iso_currency_code`` or
    ``unofficial_currency_code``"""


class BaseReportAverageMonthlyBalancesDict(TypedDict):
    start_date: str
    end_date: str
    average_balance: CreditAmountWithCurrencyDict
