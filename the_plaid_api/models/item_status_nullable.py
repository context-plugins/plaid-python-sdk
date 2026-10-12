from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .item_status_investments import ItemStatusInvestments, ItemStatusInvestmentsDict
from .item_status_last_webhook import ItemStatusLastWebhook, ItemStatusLastWebhookDict
from .item_status_transactions import ItemStatusTransactions, ItemStatusTransactionsDict


class ItemStatusNullable(SdkBaseModel):
    """An object with information about the status of the Item."""

    investments: OptionalNullable[ItemStatusInvestments] = UNSET
    """Information about the last successful and failed investments update for the Item."""

    transactions: OptionalNullable[ItemStatusTransactions] = UNSET
    """Information about the last successful and failed transactions update for the Item."""

    last_webhook: OptionalNullable[ItemStatusLastWebhook] = UNSET
    """Information about the last webhook fired for the Item."""


class ItemStatusNullableDict(TypedDict):
    investments: NotRequired[ItemStatusInvestmentsDict | None]
    transactions: NotRequired[ItemStatusTransactionsDict | None]
    last_webhook: NotRequired[ItemStatusLastWebhookDict | None]
