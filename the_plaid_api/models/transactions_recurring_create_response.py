from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_stream import TransactionStream, TransactionStreamDict


class TransactionsRecurringCreateResponse(SdkBaseModel):
    """TransactionsRecurringCreateResponse defines the response schema for the
    ``/transactions/recurring/streams/create`` endpoint."""

    added_streams: list[TransactionStream]
    """Streams created as a result of the operation."""

    modified_streams: Optional[list[TransactionStream]] = UNSET
    """Other streams with transactions removed from them as a result of the operation (in no particular order)."""

    removed_stream_ids: Optional[list[str]] = UNSET
    """The ids of streams that are no longer qualified as recurring transaction streams (in no particular order)."""


class TransactionsRecurringCreateResponseDict(TypedDict):
    added_streams: list[TransactionStreamDict]
    modified_streams: NotRequired[list[TransactionStreamDict]]
    removed_stream_ids: NotRequired[list[str]]
