from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .cra_verification_income_transaction_outlier import (
    CraVerificationIncomeTransactionOutlier,
    CraVerificationIncomeTransactionOutlierDict,
)


class CraVerificationIncomeTransaction(SdkBaseModel):
    """The transaction data for an income stream."""

    transaction_id: str
    """The unique ID of the transaction. Like all Plaid identifiers, the ``transaction_id`` is case sensitive."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    account_id: str
    """Plaid's unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    amount: float
    """The settled value of the transaction, denominated in the transaction's currency as stated in
    ``iso_currency_code`` or ``unofficial_currency_code``. Positive values when money moves out of the account; negative
    values when money moves in. For example, credit card purchases are positive; credit card payment, direct deposits,
    and refunds are negative."""

    date: Date
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the
    transaction posted. Both dates are returned in an ISO 8601 format (YYYY-MM-DD)."""

    original_description: str
    """The string returned by the financial institution to describe the transaction."""

    iso_currency_code: str | None
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""

    outlier: CraVerificationIncomeTransactionOutlier
    """Metadata on whether this income transaction is an outlier."""


class CraVerificationIncomeTransactionDict(TypedDict):
    transaction_id: str
    item_id: str
    account_id: str
    amount: float
    date: Date
    original_description: str
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    outlier: CraVerificationIncomeTransactionOutlier | CraVerificationIncomeTransactionOutlierDict
