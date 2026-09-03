from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class InitialUpdateWebhook(SdkBaseModel):
    """Fired when an Item's initial transaction pull is completed. Once this webhook has been fired, transaction data
    for the most recent 30 days can be fetched for the Item. This webhook will also be fired if account selections for
    the Item are updated, with ``new_transactions`` set to the number of net new transactions pulled after the account
    selection update.

    This webhook is intended for use with ``/transactions/get``; if you are using the newer ``/transactions/sync``
    endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for
    and respond to the ``SYNC_UPDATES_AVAILABLE`` webhook instead."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``INITIAL_UPDATE``"""

    error: OptionalNullable[str] = UNSET
    """The error code associated with the webhook."""

    new_transactions: float
    """The number of new transactions available."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class InitialUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[str | None]
    new_transactions: float
    item_id: str
    environment: WebhookEnvironmentValuesOrStr
