from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransactionsRecurringUpdateInput(SdkBaseModel):
    """TransactionsRecurringUpdateInput defines a single operation to the ``/transactions/recurring/streams/update``
    endpoint."""

    stream_id: str
    """ID of the stream that all the transactions will be added into."""

    transaction_ids: list[str]
    """IDs of all the transactions that will be added into the stream. If any transaction currently exists in another
    stream, it will be removed from the other stream."""


class TransactionsRecurringUpdateInputDict(TypedDict):
    stream_id: str
    transaction_ids: list[str]
