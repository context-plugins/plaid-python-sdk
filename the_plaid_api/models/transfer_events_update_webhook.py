from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class TransferEventsUpdateWebhook(SdkBaseModel):
    """Fired when new transfer events are available. Receiving this webhook indicates you should fetch the new events
    from ``/transfer/event/sync``. If multiple transfer events occur within a single minute, only one webhook will be
    fired, so a single webhook instance may correspond to multiple transfer events."""

    webhook_type: str
    """``TRANSFER``"""

    webhook_code: str
    """``TRANSFER_EVENTS_UPDATE``"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class TransferEventsUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    environment: WebhookEnvironmentValuesOrStr
