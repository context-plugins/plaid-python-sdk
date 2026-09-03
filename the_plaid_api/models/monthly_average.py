from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MonthlyAverage(SdkBaseModel):
    """The monthly average amount calculated by dividing the total by the number of calendar months in the time
    period."""

    amount: OptionalNullable[float] = UNSET
    """The monthly average amount of all the aggregated transactions of the given category, across all the accounts for
    the given time window.

    The average is calculated by dividing the total amount of the transactions by the number of calendar months in the
    given time window."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the amount. Always ``null`` if ``unofficial_currency_code`` is non-``null``."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the amount. Always ``null`` if ``iso_currency_code`` is
    non-``null``.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""


class MonthlyAverageDict(TypedDict):
    amount: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
