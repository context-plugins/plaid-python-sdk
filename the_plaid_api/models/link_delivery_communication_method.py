from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.link_delivery_delivery_method import LinkDeliveryDeliveryMethodOrStr


class LinkDeliveryCommunicationMethod(SdkBaseModel):
    """The communication method containing both the type and address to send the URL."""

    method: Optional[LinkDeliveryDeliveryMethodOrStr] = UNSET
    """The delivery method to be used to deliver the Hosted Link session URL.

    ``SMS``: The URL will be delivered through SMS

    ``EMAIL``: The URL will be delivered through email"""

    address: Optional[str] = UNSET
    """The phone number / email address that Hosted Link sessions are delivered to. Phone numbers must be in E.164
    format."""


class LinkDeliveryCommunicationMethodDict(TypedDict):
    method: NotRequired[LinkDeliveryDeliveryMethodOrStr]
    address: NotRequired[str]
