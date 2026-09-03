from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .business_account import BusinessAccount, BusinessAccountDict
from .cashflow_report_transaction import CashflowReportTransaction, CashflowReportTransactionDict
from .item import Item, ItemDict


class CashflowReportTransactionsGetResponse(SdkBaseModel):
    """CashflowReportTransactionsGetResponse defines the response schema for ``/cashflow_report/transactions/get``"""

    accounts: list[BusinessAccount]
    """An array containing the ``accounts`` associated with the Item for which transactions are being returned. Each
    transaction can be mapped to its corresponding account via the ``account_id`` field."""

    transactions: list[CashflowReportTransaction]
    """An array containing transactions from the account. Transactions are returned in reverse chronological order, with
    the most recent at the beginning of the array. The maximum number of transactions returned is determined by the
    ``count`` parameter."""

    total_transactions: int
    """The total number of transactions available within the date range specified. If ``total_transactions`` is larger
    than the size of the ``transactions`` array, more transactions are available and can be fetched using the ``cursor``
    parameter."""

    item: Item
    """Metadata about the Item."""

    next_cursor: str
    """Cursor used for fetching any future updates after the latest update provided in this response."""

    has_more: bool
    """Represents if more than requested count of transactions exists to be fetched"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CashflowReportTransactionsGetResponseDict(TypedDict):
    accounts: list[BusinessAccount | BusinessAccountDict]
    transactions: list[CashflowReportTransaction | CashflowReportTransactionDict]
    total_transactions: int
    item: Item | ItemDict
    next_cursor: str
    has_more: bool
    request_id: str
