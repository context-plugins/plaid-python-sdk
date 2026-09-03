from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class ProcessorRecurringTransactionsUpdateWebhook(SdkBaseModel):
    """This webhook is only sent to `Plaid processor partners <https://plaid.com/docs/auth/partnerships/>`__.

    Fired when recurring transactions data is updated. This includes when a new recurring stream is detected or when a
    new transaction is added to an existing recurring stream. The ``RECURRING_TRANSACTIONS_UPDATE`` webhook will also
    fire when one or more attributes of the recurring stream changes, which is usually a result of the addition, update,
    or removal of transactions to the stream.

    After receipt of this webhook, the updated data can be fetched from ``/processor/transactions/recurring/get``."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``RECURRING_TRANSACTIONS_UPDATE``"""

    account_id: str
    """The ID of the account."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ProcessorRecurringTransactionsUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    account_id: str
    environment: WebhookEnvironmentValuesOrStr
