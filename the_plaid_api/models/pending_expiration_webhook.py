from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class PendingExpirationWebhook(SdkBaseModel):
    """Fired when an Item's access consent is expiring in 7 days. This can be resolved by having the user go through
    Link's update mode. This webhook is fired only for Items associated with institutions in Europe (including the UK);
    for Items associated with institutions in the US or Canada, see https://plaid.com/docs/api/items/#pending_disconnect
    instead."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``PENDING_EXPIRATION``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    consent_expiration_time: RFC3339DateTime
    """The date and time at which the Item's access consent will expire, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class PendingExpirationWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    consent_expiration_time: RFC3339DateTime
    environment: WebhookEnvironmentValuesOrStr
