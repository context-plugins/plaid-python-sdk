from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class BaseReportHistoricalBalance(SdkBaseModel):
    """An object representing a balance held by an account in the past"""

    date: Date
    """The date of the calculated historical balance, in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (YYYY-MM-DD)"""

    current: float
    """The total amount of funds in the account, calculated from the ``current`` balance in the ``balance`` object by
    subtracting inflows and adding back outflows according to the posted date of each transaction.

    If the account has any pending transactions, historical balance amounts on or after the date of the earliest pending
    transaction may differ if retrieved in subsequent Asset Reports as a result of those pending transactions
    posting."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the balance. Always ``null`` if ``unofficial_currency_code`` is non-``null``."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the balance. Always ``null`` if ``iso_currency_code`` is
    non-``null``.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""


class BaseReportHistoricalBalanceDict(TypedDict):
    date: Date
    current: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
