from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.pending_disconnect_webhook_reason import PendingDisconnectWebhookReasonOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class PendingDisconnectWebhook(SdkBaseModel):
    """Fired when an Item is expected to be disconnected. The webhook will currently be fired 7 days before the existing
    Item is scheduled for disconnection. This can be resolved by having the user go through Link's `update mode
    <https://plaid.com/docs/link/update-mode>`__. Currently, this webhook is fired only for US or Canadian institutions;
    in the UK or EU, you should continue to listen for the https://plaid.com/docs/api/items/#pending_expiration webhook
    instead."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``PENDING_DISCONNECT``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    reason: PendingDisconnectWebhookReasonOrStr
    """Reason why the Item is about to be disconnected. ``INSTITUTION_MIGRATION``: The institution is moving to API or
    to a different integration. For example, this can occur when an institution moves from a non-OAuth integration to an
    OAuth integration. ``INSTITUTION_TOKEN_EXPIRATION``: The consent on an Item associated with a US or CA institution
    is about to expire."""

    disconnect_time: RFC3339DateTime
    """The date and time at which the Item is scheduled to disconnect, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class PendingDisconnectWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    reason: PendingDisconnectWebhookReasonOrStr
    disconnect_time: RFC3339DateTime
    environment: WebhookEnvironmentValuesOrStr
