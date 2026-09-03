from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_stream import TransactionStream, TransactionStreamDict


class TransactionsRecurringUpdateResponse(SdkBaseModel):
    """TransactionsRecurringUpdateResponse defines the response schema for the
    ``/transactions/recurring/streams/update`` endpoint."""

    modified_streams: list[TransactionStream]
    """Directly modified stream, along with other streams with transactions removed from them as a result of the
    operation (in no particular order)."""

    removed_stream_ids: Optional[list[str]] = UNSET
    """The ids of streams that are no longer qualified as recurring transaction streams (in no particular order)."""


class TransactionsRecurringUpdateResponseDict(TypedDict):
    modified_streams: list[TransactionStream | TransactionStreamDict]
    removed_stream_ids: NotRequired[list[str]]
