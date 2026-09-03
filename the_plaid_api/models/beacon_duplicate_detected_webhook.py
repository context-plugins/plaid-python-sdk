from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BeaconDuplicateDetectedWebhook(SdkBaseModel):
    """Fired when a Beacon User created within your organization matches one of your existing users."""

    webhook_type: str
    """``BEACON``"""

    webhook_code: str
    """``DUPLICATE_DETECTED``"""

    beacon_duplicate_id: str
    """The ID of the associated Beacon Duplicate."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BeaconDuplicateDetectedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    beacon_duplicate_id: str
    environment: WebhookEnvironmentValuesOrStr
