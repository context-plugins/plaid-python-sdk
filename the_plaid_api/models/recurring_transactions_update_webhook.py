from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class RecurringTransactionsUpdateWebhook(SdkBaseModel):
    """Fired when recurring transactions data is updated. This includes when a new recurring stream is detected or when
    a new transaction is added to an existing recurring stream. The ``RECURRING_TRANSACTIONS_UPDATE`` webhook will also
    fire when one or more attributes of the recurring stream changes, which is usually a result of the addition, update,
    or removal of transactions to the stream.

    After receipt of this webhook, the updated data can be fetched from ``/transactions/recurring/get``."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``RECURRING_TRANSACTIONS_UPDATE``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    account_ids: list[str]
    """A list of ``account_ids`` for accounts that have new or updated recurring transactions data."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class RecurringTransactionsUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    account_ids: list[str]
    environment: WebhookEnvironmentValuesOrStr
