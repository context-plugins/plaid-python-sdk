from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PayStubDeductionsBreakdown(SdkBaseModel):
    """An object representing the deduction line items for the pay period"""

    current_amount: float | None
    """Raw amount of the deduction"""

    description: str | None
    """Description of the deduction line item"""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the line item. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the line item. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    ytd_amount: float | None
    """The year-to-date amount of the deduction"""


class PayStubDeductionsBreakdownDict(TypedDict):
    current_amount: float | None
    description: str | None
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    ytd_amount: float | None
