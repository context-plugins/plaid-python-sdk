from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class FallbackAuthMicrodepositAutoVerifiedWebhook(SdkBaseModel):
    """Fires when an account is automatically verified using micro-deposits"""

    webhook_type: str
    """``AUTH``"""

    webhook_code: str
    """``AUTOMATICALLY_VERIFIED``"""

    error: OptionalNullable[str] = UNSET
    """The error code associated with the webhook."""

    account_id: str
    """The external account ID associated with the micro-deposit"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class FallbackAuthMicrodepositAutoVerifiedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[str | None]
    account_id: str
    item_id: str
    environment: WebhookEnvironmentValuesOrStr
