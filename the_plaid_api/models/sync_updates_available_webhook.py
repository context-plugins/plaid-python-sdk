from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class SyncUpdatesAvailableWebhook(SdkBaseModel):
    """Fired when an Item's transactions change. This can be due to any event resulting in new changes, such as an
    initial 30-day transactions fetch upon the initialization of an Item with transactions, the backfill of historical
    transactions that occurs shortly after, or when changes are populated from a regularly-scheduled transactions update
    job. It is recommended to listen for the ``SYNC_UPDATES_AVAILABLE`` webhook when using the ``/transactions/sync``
    endpoint. Note that when using ``/transactions/sync`` the older webhooks ``INITIAL_UPDATE``, ``HISTORICAL_UPDATE``,
    ``DEFAULT_UPDATE``, and ``TRANSACTIONS_REMOVED``, which are intended for use with ``/transactions/get``, will also
    continue to be sent in order to maintain backwards compatibility. It is not necessary to listen for and respond to
    those webhooks when using ``/transactions/sync``.

    After receipt of this webhook, the new changes can be fetched for the Item from ``/transactions/sync``.

    Note that to receive this webhook for an Item, ``/transactions/sync`` must have been called at least once on that
    Item. This means that, unlike the ``INITIAL_UPDATE`` and ``HISTORICAL_UPDATE`` webhooks, it will not fire
    immediately upon Item creation. If ``/transactions/sync`` is called on an Item that was *not* initialized with
    Transactions, the webhook will fire twice: once the first 30 days of transactions data has been fetched, and a
    second time when all available historical transactions data has been fetched.

    This webhook will fire in the Sandbox environment as it would in Production. It can also be manually triggered in
    Sandbox by calling ``/sandbox/item/fire_webhook``."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``SYNC_UPDATES_AVAILABLE``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    initial_update_complete: bool
    """Indicates if initial pull information (most recent 30 days of transaction history) is available."""

    historical_update_complete: bool
    """Indicates if historical pull information (maximum transaction history requested, up to 2 years) is available."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class SyncUpdatesAvailableWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    initial_update_complete: bool
    historical_update_complete: bool
    environment: WebhookEnvironmentValuesOrStr
