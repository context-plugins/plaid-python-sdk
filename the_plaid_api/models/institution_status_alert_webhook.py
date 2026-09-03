from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class InstitutionStatusAlertWebhook(SdkBaseModel):
    """Fired when institution status meets the conditions configured in the developer dashboard."""

    webhook_type: str
    """``DASHBOARD_CONFIGURED_ALERT``"""

    webhook_code: str
    """``INSTITUTION_STATUS_ALERT_TRIGGERED``"""

    institution_id: str
    """The ID of the associated institution."""

    institution_overall_success_rate: float
    """The global success rate of the institution, calculated based on item add health."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class InstitutionStatusAlertWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    institution_id: str
    institution_overall_success_rate: float
    environment: WebhookEnvironmentValuesOrStr
