from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class ScreeningStatusUpdatedWebhook(SdkBaseModel):
    """Fired when an individual screening status has changed, which can occur manually via the dashboard or during
    ongoing monitoring."""

    webhook_type: str
    """``SCREENING``"""

    webhook_code: str
    """``STATUS_UPDATED``"""

    screening_id: str
    """The ID of the associated screening."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ScreeningStatusUpdatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    screening_id: str
    environment: WebhookEnvironmentValuesOrStr
