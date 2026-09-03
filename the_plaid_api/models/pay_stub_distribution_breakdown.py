from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PayStubDistributionBreakdown(SdkBaseModel):
    """Information about the accounts that the payment was distributed to."""

    account_name: str | None
    """Name of the account for the given distribution."""

    bank_name: str | None
    """The name of the bank that the payment is being deposited to."""

    current_amount: float | None
    """The amount distributed to this account."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the net pay. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    mask: str | None
    """The last 2-4 alphanumeric characters of an account's official account number."""

    type_: str | None = Field(alias="type")
    """Type of the account that the paystub was sent to (e.g. 'checking')."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the net pay. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""


class PayStubDistributionBreakdownDict(TypedDict):
    account_name: str | None
    bank_name: str | None
    current_amount: float | None
    iso_currency_code: str | None
    mask: str | None
    type_: str | None
    unofficial_currency_code: str | None
