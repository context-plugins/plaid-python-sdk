from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionsRecurringCreateInput(SdkBaseModel):
    """TransactionsRecurringCreateInput defines a single input to the ``/transactions/recurring/streams/create``
    endpoint."""

    transaction_ids: Optional[list[str]] = UNSET
    """IDs of all the transactions that will be merged into one stream. If any transaction currently exists in another
    stream, it will be removed from the other stream."""


class TransactionsRecurringCreateInputDict(TypedDict):
    transaction_ids: NotRequired[list[str]]
