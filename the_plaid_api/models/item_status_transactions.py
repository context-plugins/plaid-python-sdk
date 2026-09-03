from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ItemStatusTransactions(SdkBaseModel):
    """Information about the last successful and failed transactions update for the Item."""

    last_successful_update: OptionalNullable[RFC3339DateTime] = UNSET
    """`ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ timestamp of the last successful transactions update for the
    Item. The status will update each time Plaid successfully connects with the institution, regardless of whether any
    new data is available in the update. This field does not reflect transactions updates performed by non-Transactions
    products (e.g. Signal)."""

    last_failed_update: OptionalNullable[RFC3339DateTime] = UNSET
    """`ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ timestamp of the last failed transactions update for the Item.
    The status will update each time Plaid fails an attempt to connect with the institution, regardless of whether any
    new data is available in the update. This field does not reflect transactions updates performed by non-Transactions
    products (e.g. Signal)."""


class ItemStatusTransactionsDict(TypedDict):
    last_successful_update: NotRequired[RFC3339DateTime | None]
    last_failed_update: NotRequired[RFC3339DateTime | None]
