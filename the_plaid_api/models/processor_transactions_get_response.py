from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .transaction import Transaction, TransactionDict


class ProcessorTransactionsGetResponse(SdkBaseModel):
    """ProcessorTransactionsGetResponse defines the response schema for ``/processor/transactions/get``"""

    account: Account
    """A single account at a financial institution."""

    transactions: list[Transaction]
    """An array containing transactions from the account. Transactions are returned in reverse chronological order, with
    the most recent at the beginning of the array. The maximum number of transactions returned is determined by the
    ``count`` parameter."""

    total_transactions: int
    """The total number of transactions available within the date range specified. If ``total_transactions`` is larger
    than the size of the ``transactions`` array, more transactions are available and can be fetched via manipulating the
    ``offset`` parameter."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorTransactionsGetResponseDict(TypedDict):
    account: Account | AccountDict
    transactions: list[Transaction | TransactionDict]
    total_transactions: int
    request_id: str
