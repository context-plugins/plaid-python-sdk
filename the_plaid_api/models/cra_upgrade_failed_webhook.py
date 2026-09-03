from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class CraUpgradeFailedWebhook(SdkBaseModel):
    """Fired when a Check Report upgrade attempt has failed"""

    webhook_type: str
    """``CHECK_REPORT``"""

    webhook_code: str
    """``UPGRADE_FAILED``"""

    user_id: str
    """The ``user_id`` corresponding to the user the webhook has fired for."""

    item_ids: list[str]
    """An array of ``item_id``s for items that failed to be upgraded by a Check Report upgrade attempt."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CraUpgradeFailedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    item_ids: list[str]
    environment: WebhookEnvironmentValuesOrStr
