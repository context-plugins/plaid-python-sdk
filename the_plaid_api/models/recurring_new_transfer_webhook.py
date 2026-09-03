from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class RecurringNewTransferWebhook(SdkBaseModel):
    """Fired when a new transfer of a recurring transfer is originated."""

    webhook_type: str
    """``TRANSFER``"""

    webhook_code: str
    """``RECURRING_NEW_TRANSFER``"""

    recurring_transfer_id: str
    """Plaid's unique identifier for a recurring transfer."""

    transfer_id: str
    """Plaid's unique identifier for a transfer."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class RecurringNewTransferWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    recurring_transfer_id: str
    transfer_id: str
    environment: WebhookEnvironmentValuesOrStr
