from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class ItemAddResultWebhook(SdkBaseModel):
    """Fired when a user successfully adds a Plaid Item during a Link session when using Hosted Link or Multi-Item Link
    sessions. Contains the public token for the Item."""

    webhook_type: str
    """``LINK``"""

    webhook_code: str
    """``ITEM_ADD_RESULT``"""

    link_session_id: str
    """The identifier for the Link session."""

    link_token: str
    """The ``link_token`` used to create the Link session."""

    public_token: str
    """The ``public_token`` corresponding to the Item that was added."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ItemAddResultWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    link_session_id: str
    link_token: str
    public_token: str
    environment: WebhookEnvironmentValuesOrStr
