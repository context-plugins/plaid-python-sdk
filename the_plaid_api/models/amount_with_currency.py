from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AmountWithCurrency(SdkBaseModel):
    """A monetary amount with its associated currency information, supporting both official and unofficial currency
    codes."""

    amount: OptionalNullable[float] = UNSET
    """If the parent object represents a category of transactions, such as ``total_amount``, ``transfers_in``,
    ``total_income``, etc. the ``amount`` represents the sum of all of the transactions in the group.

    If the parent object is ``cash_flow``, the ``amount`` represents the total value of all the inflows minus all the
    outflows across all the accounts in the report in the given time window.

    If the parent object is ``minimum_balance``, the ``amount`` represents the lowest balance of the account during the
    given time window."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the amount. Always ``null`` if ``unofficial_currency_code`` is non-``null``."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the amount. Always ``null`` if ``iso_currency_code`` is
    non-``null``.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""


class AmountWithCurrencyDict(TypedDict):
    amount: NotRequired[float | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
