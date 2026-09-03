from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BeaconReportCreatedWebhook(SdkBaseModel):
    """Fired when one of your Beacon Users is first reported to the Beacon network."""

    webhook_type: str
    """``BEACON``"""

    webhook_code: str
    """``REPORT_CREATED``"""

    beacon_report_id: str
    """The ID of the associated Beacon Report."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BeaconReportCreatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    beacon_report_id: str
    environment: WebhookEnvironmentValuesOrStr
