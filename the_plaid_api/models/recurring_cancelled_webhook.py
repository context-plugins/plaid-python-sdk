from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class RecurringCancelledWebhook(SdkBaseModel):
    """Fired when a recurring transfer is cancelled by Plaid."""

    webhook_type: str
    """``TRANSFER``"""

    webhook_code: str
    """``RECURRING_CANCELLED``"""

    recurring_transfer_id: str
    """Plaid's unique identifier for a recurring transfer."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class RecurringCancelledWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    recurring_transfer_id: str
    environment: WebhookEnvironmentValuesOrStr
