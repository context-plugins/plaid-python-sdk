from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .pay import Pay, PayDict


class EarningsTotal(SdkBaseModel):
    """An object representing both the current pay period and year to date amount for an earning category."""

    current_amount: OptionalNullable[float] = UNSET
    """Total amount of the earnings for this pay period"""

    current_pay: Optional[Pay] = UNSET
    """An object representing a monetary amount."""

    ytd_pay: Optional[Pay] = UNSET
    """An object representing a monetary amount."""

    hours: OptionalNullable[float] = UNSET
    """Total number of hours worked for this pay period"""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the line item. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the line item. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    ytd_amount: OptionalNullable[float] = UNSET
    """The total year-to-date amount of the earnings"""


class EarningsTotalDict(TypedDict):
    current_amount: NotRequired[float | None]
    current_pay: NotRequired[Pay | PayDict]
    ytd_pay: NotRequired[Pay | PayDict]
    hours: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    ytd_amount: NotRequired[float | None]
