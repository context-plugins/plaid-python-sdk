from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BeaconReportSyndicationCreatedWebhook(SdkBaseModel):
    """Fired when a report created on the Beacon Network matches with one of your Beacon Users."""

    webhook_type: str
    """``BEACON``"""

    webhook_code: str
    """``REPORT_SYNDICATION_CREATED``"""

    beacon_report_syndication_id: str
    """The ID of the associated Beacon Report Syndication."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BeaconReportSyndicationCreatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    beacon_report_syndication_id: str
    environment: WebhookEnvironmentValuesOrStr
