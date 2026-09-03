from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class ItemLoginRepairedWebhook(SdkBaseModel):
    """Fired when an Item has exited the ``ITEM_LOGIN_REQUIRED`` state without the user having gone through the update
    mode flow in your app (this can happen if the user completed the update mode in a different app). If you have
    messaging that tells the user to complete the update mode flow, you should silence this messaging upon receiving the
    ``LOGIN_REPAIRED`` webhook."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``LOGIN_REPAIRED``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ItemLoginRepairedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    environment: WebhookEnvironmentValuesOrStr
