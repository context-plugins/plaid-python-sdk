from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class HostedMmdverificationWebhook(SdkBaseModel):
    """Contains the state of an SMS Same-Day Micro-deposits verification session."""

    webhook_type: str
    """``AUTH``"""

    webhook_code: str
    """``SMS_MICRODEPOSITS_VERIFICATION``"""

    status: str
    """The final status of the Same-Day Micro-deposits verification. Will always be ``MANUALLY_VERIFIED`` or
    ``VERIFICATION_FAILED``."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    account_id: str
    """The external account ID of the affected account"""

    environment: Optional[WebhookEnvironmentValuesOrStr] = UNSET
    """The Plaid environment the webhook was sent from"""


class HostedMmdverificationWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    status: str
    item_id: str
    account_id: str
    environment: NotRequired[WebhookEnvironmentValuesOrStr]
