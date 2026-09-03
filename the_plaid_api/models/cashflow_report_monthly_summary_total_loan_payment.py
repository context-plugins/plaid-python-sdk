from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CashflowReportMonthlySummaryTotalLoanPayment(SdkBaseModel):
    """The total amount of all loan payment transactions during this month."""

    amount: float
    """Value of amount with up to 2 decimal places."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the amount. Always ``null`` if ``unofficial_currency_code`` is non-``null``"""

    unofficial_currency_code: str | None
    """The unofficial currency code of the amount. Always ``null`` if ``iso_currency_code`` is non-``null``. Unofficial
    currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and
    the currencies of certain countries."""


class CashflowReportMonthlySummaryTotalLoanPaymentDict(TypedDict):
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
