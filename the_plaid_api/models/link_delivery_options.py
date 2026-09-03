from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_delivery_recipient import LinkDeliveryRecipient, LinkDeliveryRecipientDict


class LinkDeliveryOptions(SdkBaseModel):
    """Optional metadata related to the Hosted Link session"""

    recipient: Optional[LinkDeliveryRecipient] = UNSET
    """Metadata related to the recipient. If the information required to populate this field is not available, leave it
    blank."""


class LinkDeliveryOptionsDict(TypedDict):
    recipient: NotRequired[LinkDeliveryRecipient | LinkDeliveryRecipientDict]
