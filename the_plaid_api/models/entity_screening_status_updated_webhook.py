from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class EntityScreeningStatusUpdatedWebhook(SdkBaseModel):
    """Fired when an entity screening status has changed, which can occur manually via the dashboard or during ongoing
    monitoring."""

    webhook_type: str
    """``ENTITY_SCREENING``"""

    webhook_code: str
    """``STATUS_UPDATED``"""

    entity_screening_id: str
    """The ID of the associated entity screening."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class EntityScreeningStatusUpdatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    entity_screening_id: str
    environment: WebhookEnvironmentValuesOrStr
