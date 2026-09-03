from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class CraPartnerInsightsErrorWebhook(SdkBaseModel):
    """Fired when a partner insights report has failed to generate"""

    webhook_type: str
    """``CRA_INSIGHTS``"""

    webhook_code: str
    """``PARTNER_INSIGHTS_ERROR``"""

    user_id: str
    """The ``user_id`` corresponding to the user the webhook has fired for."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CraPartnerInsightsErrorWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    environment: WebhookEnvironmentValuesOrStr
