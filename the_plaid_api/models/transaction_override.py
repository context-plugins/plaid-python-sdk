from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class TransactionOverride(SdkBaseModel):
    """Data to populate as test transaction data. If not specified, random transactions will be generated instead."""

    date_transacted: Date
    """The date of the transaction, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format.
    Transactions in Sandbox will move from pending to posted once their transaction date has been reached. If a
    ``date_transacted`` is not provided by the institution, a transaction date may be available in the
    https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-authorized-date field."""

    date_posted: Date
    """The date the transaction posted, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format.
    Posted dates in the past or present will result in posted transactions; posted dates in the future will result in
    pending transactions."""

    amount: float
    """The transaction amount. Can be negative."""

    description: str
    """The transaction description."""

    currency: Optional[str] = UNSET
    """The ISO-4217 format currency code for the transaction."""


class TransactionOverrideDict(TypedDict):
    date_transacted: Date
    date_posted: Date
    amount: float
    description: str
    currency: NotRequired[str]
