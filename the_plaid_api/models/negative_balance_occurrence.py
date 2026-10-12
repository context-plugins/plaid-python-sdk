from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .amount_with_currency import AmountWithCurrency, AmountWithCurrencyDict


class NegativeBalanceOccurrence(SdkBaseModel):
    """Details about a specific occurrence of a negative balance period, including start and end dates."""

    start_date: OptionalNullable[Date] = UNSET
    """The date of the first transaction that caused the account to have a negative balance. The date will be returned
    in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: OptionalNullable[Date] = UNSET
    """The date of the last transaction that caused the account to have a negative balance. The date will be returned in
    an ISO 8601 format (YYYY-MM-DD). This date is inclusive, meaning that this was the last date that the account had a
    negative balance."""

    minimum_balance: OptionalNullable[AmountWithCurrency] = UNSET
    """A monetary amount with its associated currency information, supporting both official and unofficial currency
    codes."""


class NegativeBalanceOccurrenceDict(TypedDict):
    start_date: NotRequired[Date | None]
    end_date: NotRequired[Date | None]
    minimum_balance: NotRequired[AmountWithCurrencyDict | None]
