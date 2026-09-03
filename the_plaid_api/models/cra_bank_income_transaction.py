from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.cra_bank_income_bonus_type import CraBankIncomeBonusTypeOrStr


class CraBankIncomeTransaction(SdkBaseModel):
    """The transactions data for the end user's income source(s)."""

    transaction_id: str
    """The unique ID of the transaction. Like all Plaid identifiers, the ``transaction_id`` is case sensitive."""

    amount: float
    """The settled value of the transaction, denominated in the transaction's currency as stated in
    ``iso_currency_code`` or ``unofficial_currency_code``. Positive values when money moves out of the account; negative
    values when money moves in. For example, credit card purchases are positive; credit card payment, direct deposits,
    and refunds are negative."""

    date: Date
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the
    transaction posted. Both dates are returned in an ISO 8601 format (YYYY-MM-DD)."""

    name: Optional[str] = UNSET
    """The merchant name or transaction description. This is a legacy field that is no longer maintained. For merchant
    name, use the ``merchant_name`` field; for description, use the ``original_description`` field."""

    original_description: str | None
    """The string returned by the financial institution to describe the transaction."""

    pending: bool
    """When true, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount,
    category ID) may change before they are settled."""

    check_number: OptionalNullable[str] = UNSET
    """The check number of the transaction. This field is only populated for check transactions."""

    iso_currency_code: str | None
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""

    bonus_type: OptionalNullable[CraBankIncomeBonusTypeOrStr] = UNSET
    """The type of bonus that this transaction represents, if it is a bonus. ``BONUS_INCLUDED``: Bonus is included in
    this transaction along with the normal pay ``BONUS_ONLY``: This transaction is a standalone bonus"""


class CraBankIncomeTransactionDict(TypedDict):
    transaction_id: str
    amount: float
    date: Date
    name: NotRequired[str]
    original_description: str | None
    pending: bool
    check_number: NotRequired[str | None]
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    bonus_type: NotRequired[CraBankIncomeBonusTypeOrStr | None]
