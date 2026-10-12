from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .amount_with_currency import AmountWithCurrency, AmountWithCurrencyDict


class MonthlySummary(SdkBaseModel):
    """Monthly summary of transactions within a specific time period, showing aggregated amounts."""

    start_date: OptionalNullable[Date] = UNSET
    """The start date of the month for the given report time window. Will be provided in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    end_date: OptionalNullable[Date] = UNSET
    """The end date of the month for the given report time window. Will be provided in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    total_amount: OptionalNullable[AmountWithCurrency] = UNSET
    """A monetary amount with its associated currency information, supporting both official and unofficial currency
    codes."""


class MonthlySummaryDict(TypedDict):
    start_date: NotRequired[Date | None]
    end_date: NotRequired[Date | None]
    total_amount: NotRequired[AmountWithCurrencyDict | None]
