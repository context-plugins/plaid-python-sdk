from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DeductionsBreakdown(SdkBaseModel):
    """An object representing the deduction line items for the pay period"""

    current_amount: OptionalNullable[float] = UNSET
    """Raw amount of the deduction"""

    description: OptionalNullable[str] = UNSET
    """Description of the deduction line item"""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the line item. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the line item. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    ytd_amount: OptionalNullable[float] = UNSET
    """The year-to-date amount of the deduction"""


class DeductionsBreakdownDict(TypedDict):
    current_amount: NotRequired[float | None]
    description: NotRequired[str | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    ytd_amount: NotRequired[float | None]
