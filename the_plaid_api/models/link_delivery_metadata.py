from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.link_delivery_webhook_communication_method import LinkDeliveryWebhookCommunicationMethodOrStr
from .enums.link_delivery_webhook_delivery_status import LinkDeliveryWebhookDeliveryStatusOrStr


class LinkDeliveryMetadata(SdkBaseModel):
    """Information related to the delivery of the link session to users"""

    communication_method: Optional[LinkDeliveryWebhookCommunicationMethodOrStr] = UNSET
    """The communication method used to deliver the Hosted Link session"""

    delivery_status: Optional[LinkDeliveryWebhookDeliveryStatusOrStr] = UNSET
    """The status of the delivery of the Hosted Link to the user"""


class LinkDeliveryMetadataDict(TypedDict):
    communication_method: NotRequired[LinkDeliveryWebhookCommunicationMethodOrStr]
    delivery_status: NotRequired[LinkDeliveryWebhookDeliveryStatusOrStr]
