from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class IdentityVerificationStepUpdatedWebhook(SdkBaseModel):
    """Fired when an end user has completed a step of the Identity Verification process."""

    webhook_type: str
    """``IDENTITY_VERIFICATION``"""

    webhook_code: str
    """``STEP_UPDATED``"""

    identity_verification_id: str
    """The ID of the associated Identity Verification attempt."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class IdentityVerificationStepUpdatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    identity_verification_id: str
    environment: WebhookEnvironmentValuesOrStr
