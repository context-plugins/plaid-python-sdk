from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BeaconUserStatusUpdatedWebhook(SdkBaseModel):
    """Fired when a Beacon User status has changed, which can occur manually via the dashboard or when information is
    reported to the Beacon network."""

    webhook_type: str
    """``BEACON``"""

    webhook_code: str
    """``USER_STATUS_UPDATED``"""

    beacon_user_id: str
    """The ID of the associated Beacon user."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BeaconUserStatusUpdatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    beacon_user_id: str
    environment: WebhookEnvironmentValuesOrStr
