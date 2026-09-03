from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TotalReportInflowAmount(SdkBaseModel):
    """Total amount of debit transactions into the report's accounts in the time period of the report. This field only
    takes into account USD transactions from the accounts."""

    amount: float
    """Value of amount with up to 2 decimal places."""

    iso_currency_code: str | None
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""


class TotalReportInflowAmountDict(TypedDict):
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
