from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PayStubEarningsBreakdown(SdkBaseModel):
    """An object representing the earnings line items for the pay period."""

    canonical_description: str | None
    """Commonly used term to describe the earning line item."""

    current_amount: float | None
    """Raw amount of the earning line item."""

    description: str | None
    """Description of the earning line item."""

    hours: float | None
    """Number of hours applicable for this earning."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the line item. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    rate: float | None
    """Hourly rate applicable for this earning."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the line item. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    ytd_amount: float | None
    """The year-to-date amount of the line item."""


class PayStubEarningsBreakdownDict(TypedDict):
    canonical_description: str | None
    current_amount: float | None
    description: str | None
    hours: float | None
    iso_currency_code: str | None
    rate: float | None
    unofficial_currency_code: str | None
    ytd_amount: float | None
