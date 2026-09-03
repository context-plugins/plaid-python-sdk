from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class TransferPlatformOnboardingUpdateWebhook(SdkBaseModel):
    """Fired when the status of an onboarding originator has been updated. Call ``/transfer/originator/get`` to check
    the latest status"""

    webhook_type: str
    """``"TRANSFER"``"""

    webhook_code: str
    """``"PLATFORM_ONBOARDING_UPDATE"``"""

    originator_client_id: str
    """The client ID of the originator"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class TransferPlatformOnboardingUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    originator_client_id: str
    environment: WebhookEnvironmentValuesOrStr
