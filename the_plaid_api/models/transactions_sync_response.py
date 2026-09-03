from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .enums.transactions_update_status import TransactionsUpdateStatusOrStr
from .removed_transaction import RemovedTransaction, RemovedTransactionDict
from .transaction import Transaction, TransactionDict


class TransactionsSyncResponse(SdkBaseModel):
    """TransactionsSyncResponse defines the response schema for ``/transactions/sync``"""

    transactions_update_status: TransactionsUpdateStatusOrStr
    """A description of the update status for transaction pulls of an Item. This field contains the same information
    provided by transactions webhooks, and may be helpful for webhook troubleshooting or when recovering from missed
    webhooks.

    ``TRANSACTIONS_UPDATE_STATUS_UNKNOWN``: Unable to fetch transactions update status for Item. ``NOT_READY``: The Item
    is pending transaction pull. ``INITIAL_UPDATE_COMPLETE``: Initial pull for the Item is complete, historical pull is
    pending. ``HISTORICAL_UPDATE_COMPLETE``: Both initial and historical pull for Item are complete."""

    accounts: list[Account]
    """An array of accounts at a financial institution associated with the transactions in this response. Only accounts
    that have associated transactions will be shown. For example, ``investment``-type accounts will be omitted."""

    added: list[Transaction]
    """Transactions that have been added to the Item since ``cursor`` ordered by ascending last modified time."""

    modified: list[Transaction]
    """Transactions that have been modified on the Item since ``cursor`` ordered by ascending last modified time."""

    removed: list[RemovedTransaction]
    """Transactions that have been removed from the Item since ``cursor`` ordered by ascending last modified time."""

    next_cursor: str
    """Cursor used for fetching any future updates after the latest update provided in this response. The cursor
    obtained after all pages have been pulled (indicated by ``has_more`` being ``false``) will be valid for at least 1
    year. This cursor should be persisted for later calls. If transactions are not yet available, this will be an empty
    string.

    If ``account_id`` is included in the request, the returned cursor will reflect updates for that specific account."""

    has_more: bool
    """Represents if more than requested count of transaction updates exist. If true, the additional updates can be
    fetched by making an additional request with ``cursor`` set to ``next_cursor``. If ``has_more`` is true, it's
    important to pull all available pages, to make it less likely for underlying data changes to conflict with
    pagination."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsSyncResponseDict(TypedDict):
    transactions_update_status: TransactionsUpdateStatusOrStr
    accounts: list[Account | AccountDict]
    added: list[Transaction | TransactionDict]
    modified: list[Transaction | TransactionDict]
    removed: list[RemovedTransaction | RemovedTransactionDict]
    next_cursor: str
    has_more: bool
    request_id: str
