from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .link_delivery_metadata import LinkDeliveryMetadata, LinkDeliveryMetadataDict


class LinkUserDeliveryStatusWebhook(SdkBaseModel):
    """Webhook indicating that the status of the delivery of the Hosted Link session to a user"""

    webhook_type: str
    """``LINK_DELIVERY``"""

    webhook_code: str
    """``DELIVERY_STATUS``"""

    link_delivery_session_id: str
    """The ID of the Hosted Link session."""

    timestamp: str
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    link_delivery_metadata: LinkDeliveryMetadata
    """Information related to the delivery of the link session to users"""


class LinkUserDeliveryStatusWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    link_delivery_session_id: str
    timestamp: str
    link_delivery_metadata: LinkDeliveryMetadataDict
