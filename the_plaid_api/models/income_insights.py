from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .amount_with_currency import AmountWithCurrency, AmountWithCurrencyDict
from .amount_with_currency_with_monthly_average import (
    AmountWithCurrencyWithMonthlyAverage,
    AmountWithCurrencyWithMonthlyAverageDict,
)


class IncomeInsights(SdkBaseModel):
    """Comprehensive income analysis including total income, income excluding transfers, and inbound transfer
    amounts."""

    total_income: OptionalNullable[AmountWithCurrency] = UNSET
    """The total amount of all income transactions in the given time period."""

    income_excluding_transfers: OptionalNullable[AmountWithCurrencyWithMonthlyAverage] = UNSET
    """Income excluding account transfer transactions for the period, including a monthly average."""

    transfers_in: OptionalNullable[AmountWithCurrencyWithMonthlyAverage] = UNSET
    """Sum of inbound transfer transactions for the period, including a monthly average."""


class IncomeInsightsDict(TypedDict):
    total_income: NotRequired[AmountWithCurrency | AmountWithCurrencyDict | None]
    income_excluding_transfers: NotRequired[
        AmountWithCurrencyWithMonthlyAverage | AmountWithCurrencyWithMonthlyAverageDict | None
    ]
    transfers_in: NotRequired[AmountWithCurrencyWithMonthlyAverage | AmountWithCurrencyWithMonthlyAverageDict | None]
