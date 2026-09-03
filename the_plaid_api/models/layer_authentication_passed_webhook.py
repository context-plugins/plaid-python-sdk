from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class LayerAuthenticationPassedWebhook(SdkBaseModel):
    """Indicates that Plaid's authentication process has completed for a user and that Plaid has verified that the user
    owns their phone number. If you receive this webhook, you should skip your own OTP phone number verification flow
    for the user, even if the user does not complete the entire Link flow. If the user doesn't complete the full Link
    flow (as verified by your being able to successfully call ``/user_account/session/get`` using the ``public_token``
    from the ``onSuccess`` callback) it is recommended that you implement `webhook verification
    <https://plaid.com/docs/api/webhooks/webhook-verification/>`__ or another technique to avoid webhook spoofing
    attacks."""

    webhook_type: str
    """``LAYER``"""

    webhook_code: str
    """``LAYER_AUTHENTICATION_PASSED``"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""

    link_session_id: str
    """An identifier for the Link session these events occurred in"""

    link_token: str
    """The Link token used to create the Link session these events are from"""


class LayerAuthenticationPassedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    environment: WebhookEnvironmentValuesOrStr
    link_session_id: str
    link_token: str
