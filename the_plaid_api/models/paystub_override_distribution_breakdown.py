from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubOverrideDistributionBreakdown(SdkBaseModel):
    """Information about the accounts that the payment was distributed to."""

    account_name: OptionalNullable[str] = UNSET
    """Name of the account for the given distribution."""

    bank_name: OptionalNullable[str] = UNSET
    """The name of the bank that the payment is being deposited to."""

    current_amount: OptionalNullable[float] = UNSET
    """The amount distributed to this account."""

    currency: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the net pay. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    mask: OptionalNullable[str] = UNSET
    """The last 2-4 alphanumeric characters of an account's official account number."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Type of the account that the paystub was sent to (e.g. 'checking')."""


class PaystubOverrideDistributionBreakdownDict(TypedDict):
    account_name: NotRequired[str | None]
    bank_name: NotRequired[str | None]
    current_amount: NotRequired[float | None]
    currency: NotRequired[str | None]
    mask: NotRequired[str | None]
    type_: NotRequired[str | None]
