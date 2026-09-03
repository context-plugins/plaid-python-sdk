from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.earnings_breakdown_canonical_description import EarningsBreakdownCanonicalDescriptionOrStr


class EarningsBreakdown(SdkBaseModel):
    """An object representing the earnings line items for the pay period."""

    canonical_description: OptionalNullable[EarningsBreakdownCanonicalDescriptionOrStr] = UNSET
    """Commonly used term to describe the earning line item."""

    current_amount: OptionalNullable[float] = UNSET
    """Raw amount of the earning line item."""

    description: OptionalNullable[str] = UNSET
    """Description of the earning line item."""

    hours: OptionalNullable[float] = UNSET
    """Number of hours applicable for this earning."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the line item. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    rate: OptionalNullable[float] = UNSET
    """Hourly rate applicable for this earning."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the line item. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    ytd_amount: OptionalNullable[float] = UNSET
    """The year-to-date amount of the line item."""


class EarningsBreakdownDict(TypedDict):
    canonical_description: NotRequired[EarningsBreakdownCanonicalDescriptionOrStr | None]
    current_amount: NotRequired[float | None]
    description: NotRequired[str | None]
    hours: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    rate: NotRequired[float | None]
    unofficial_currency_code: NotRequired[str | None]
    ytd_amount: NotRequired[float | None]
