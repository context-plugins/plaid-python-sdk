from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel


class CreditBankIncomeTransaction(SdkBaseModel):
    """The transactions data for the end user's income source(s)."""

    amount: Optional[float] = UNSET
    """The settled value of the transaction, denominated in the transaction's currency as stated in
    ``iso_currency_code`` or ``unofficial_currency_code``. Positive values when money moves out of the account; negative
    values when money moves in. For example, credit card purchases are positive; credit card payment, direct deposits,
    and refunds are negative."""

    date: Optional[Date] = UNSET
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the
    transaction posted. Both dates are returned in an ISO 8601 format (YYYY-MM-DD)."""

    name: Optional[str] = UNSET
    """The merchant name or transaction description."""

    original_description: OptionalNullable[str] = UNSET
    """The string returned by the financial institution to describe the transaction."""

    pending: Optional[bool] = UNSET
    """When true, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount,
    category ID) may change before they are settled."""

    transaction_id: Optional[str] = UNSET
    """The unique ID of the transaction. Like all Plaid identifiers, the ``transaction_id`` is case sensitive."""

    check_number: OptionalNullable[str] = UNSET
    """The check number of the transaction. This field is only populated for check transactions."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""


class CreditBankIncomeTransactionDict(TypedDict):
    amount: NotRequired[float]
    date: NotRequired[Date]
    name: NotRequired[str]
    original_description: NotRequired[str | None]
    pending: NotRequired[bool]
    transaction_id: NotRequired[str]
    check_number: NotRequired[str | None]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
