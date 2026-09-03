from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class ProductPermissionsRequiredAuthWebhook(SdkBaseModel):
    """Fired when an ``ACCESS_NOT_GRANTED`` error is hit for Auth. The error can be resolved by putting the user through
    update mode with ``auth`` in the ``products`` array, as well as through the limited beta for update mode
    Authentication product validations."""

    webhook_type: str
    """``AUTH``"""

    webhook_code: str
    """``PRODUCT_PERMISSIONS_REQUIRED``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ProductPermissionsRequiredAuthWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    environment: WebhookEnvironmentValuesOrStr
