from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TotalReportOutflowAmount30D(SdkBaseModel):
    """Total amount of credit transactions out of the report's accounts in the last 30 days. This field only takes into
    account USD transactions from the accounts."""

    amount: float
    """Value of amount with up to 2 decimal places."""

    iso_currency_code: str | None
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""


class TotalReportOutflowAmount30DDict(TypedDict):
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
