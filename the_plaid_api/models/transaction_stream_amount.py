from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TransactionStreamAmount(SdkBaseModel):
    """Object with data pertaining to an amount on the transaction stream."""

    amount: Optional[float] = UNSET
    """Represents the numerical value of an amount."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the amount. Always ``null`` if ``unofficial_currency_code`` is non-``null``.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``iso_currency_code``s."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code of the amount. Always ``null`` if ``iso_currency_code`` is non-``null``. Unofficial
    currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and
    the currencies of certain countries."""


class TransactionStreamAmountDict(TypedDict):
    amount: NotRequired[float]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
