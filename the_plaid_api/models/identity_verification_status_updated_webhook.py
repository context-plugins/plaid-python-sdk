from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class IdentityVerificationStatusUpdatedWebhook(SdkBaseModel):
    """Fired when the status of an identity verification has been updated, which can be triggered via the dashboard or
    the API."""

    webhook_type: str
    """``IDENTITY_VERIFICATION``"""

    webhook_code: str
    """``STATUS_UPDATED``"""

    identity_verification_id: str
    """The ID of the associated Identity Verification attempt."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class IdentityVerificationStatusUpdatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    identity_verification_id: str
    environment: WebhookEnvironmentValuesOrStr
