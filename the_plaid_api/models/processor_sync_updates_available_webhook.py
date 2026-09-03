from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class ProcessorSyncUpdatesAvailableWebhook(SdkBaseModel):
    """This webhook is only sent to `Plaid processor partners <https://plaid.com/docs/auth/partnerships/>`__.

    Fired when an Item's transactions change. This can be due to any event resulting in new changes, such as an initial
    30-day transactions fetch upon the initialization of an Item with transactions, the backfill of historical
    transactions that occurs shortly after, or when changes are populated from a regularly-scheduled transactions update
    job. It is recommended to listen for the ``SYNC_UPDATES_AVAILABLE`` webhook when using the
    ``/processor/transactions/sync`` endpoint. Note that when using ``/processor/transactions/sync`` the older webhooks
    ``INITIAL_UPDATE``, ``HISTORICAL_UPDATE``, ``DEFAULT_UPDATE``, and ``TRANSACTIONS_REMOVED``, which are intended for
    use with ``/processor/transactions/get``, will also continue to be sent in order to maintain backwards
    compatibility. It is not necessary to listen for and respond to those webhooks when using
    ``/processor/transactions/sync``.

    After receipt of this webhook, the new changes can be fetched for the Item from ``/processor/transactions/sync``.

    Note that to receive this webhook for an Item, ``/processor/transactions/sync`` must have been called at least once
    on that Item. This means that, unlike the ``INITIAL_UPDATE`` and ``HISTORICAL_UPDATE`` webhooks, it will not fire
    immediately upon Item creation. If ``/processor/transactions/sync`` is called on an Item that was *not* initialized
    with Transactions, the webhook will fire twice: once the first 30 days of transactions data has been fetched, and a
    second time when all available historical transactions data has been fetched.

    This webhook will typically not fire in the Sandbox environment, due to the lack of dynamic transactions data. To
    test this webhook in Sandbox, call ``/sandbox/item/fire_webhook``."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``SYNC_UPDATES_AVAILABLE``"""

    account_id: str
    """The ID of the account."""

    initial_update_complete: bool
    """Indicates if initial pull information is available."""

    historical_update_complete: bool
    """Indicates if historical pull information is available."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ProcessorSyncUpdatesAvailableWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    account_id: str
    initial_update_complete: bool
    historical_update_complete: bool
    environment: WebhookEnvironmentValuesOrStr
