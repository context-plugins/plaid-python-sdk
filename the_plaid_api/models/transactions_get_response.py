from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .item import Item, ItemDict
from .transaction import Transaction, TransactionDict


class TransactionsGetResponse(SdkBaseModel):
    """TransactionsGetResponse defines the response schema for ``/transactions/get``"""

    accounts: list[Account]
    """An array containing the ``accounts`` associated with the Item for which transactions are being returned. Each
    transaction can be mapped to its corresponding account via the ``account_id`` field."""

    transactions: list[Transaction]
    """An array containing transactions from the account. Transactions are returned in reverse chronological order, with
    the most recent at the beginning of the array. The maximum number of transactions returned is determined by the
    ``count`` parameter."""

    total_transactions: int
    """The total number of transactions available within the date range specified. If ``total_transactions`` is larger
    than the size of the ``transactions`` array, more transactions are available and can be fetched via manipulating the
    ``offset`` parameter."""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsGetResponseDict(TypedDict):
    accounts: list[AccountDict]
    transactions: list[TransactionDict]
    total_transactions: int
    item: ItemDict
    request_id: str
