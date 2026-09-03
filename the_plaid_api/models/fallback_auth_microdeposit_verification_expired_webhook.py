from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class FallbackAuthMicrodepositVerificationExpiredWebhook(SdkBaseModel):
    """Fires when an account has an expired verification when using micro-deposits"""

    webhook_type: str
    """``AUTH``"""

    webhook_code: str
    """``VERIFICATION_EXPIRED``"""

    error: OptionalNullable[str] = UNSET
    """The error code associated with the webhook."""

    account_id: str
    """The external account ID associated with the micro-deposit"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class FallbackAuthMicrodepositVerificationExpiredWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[str | None]
    account_id: str
    item_id: str
    environment: WebhookEnvironmentValuesOrStr
