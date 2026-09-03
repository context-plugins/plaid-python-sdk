from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class CraPartnerInsightsCompleteWebhook(SdkBaseModel):
    """Fired when a partner insights report has finished generating and results are available"""

    webhook_type: str
    """``CRA_INSIGHTS``"""

    webhook_code: str
    """``PARTNER_INSIGHTS_COMPLETE``"""

    user_id: str
    """The ``user_id`` corresponding to the user the webhook has fired for."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CraPartnerInsightsCompleteWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    environment: WebhookEnvironmentValuesOrStr
