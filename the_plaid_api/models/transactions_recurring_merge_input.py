from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransactionsRecurringMergeInput(SdkBaseModel):
    """TransactionsRecurringMergeInput defines a single input to the ``/transactions/recurring/streams/merge``
    endpoint."""

    stream_ids: list[str]
    """IDs of all the streams that will be merged into the first stream. This operation will retain the ``stream_id`` of
    the first stream."""


class TransactionsRecurringMergeInputDict(TypedDict):
    stream_ids: list[str]
