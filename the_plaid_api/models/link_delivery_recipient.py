from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_delivery_communication_method import LinkDeliveryCommunicationMethod, LinkDeliveryCommunicationMethodDict


class LinkDeliveryRecipient(SdkBaseModel):
    """Metadata related to the recipient. If the information required to populate this field is not available, leave it
    blank."""

    communication_methods: Optional[list[LinkDeliveryCommunicationMethod]] = UNSET
    """The list of communication methods to send the Hosted Link session URL to. If delivery is not required, leave this
    field blank."""

    first_name: Optional[str] = UNSET
    """First name of the recipient. Will be used in the body of the email / text (if configured). If this information is
    not available, leave this field blank."""


class LinkDeliveryRecipientDict(TypedDict):
    communication_methods: NotRequired[list[LinkDeliveryCommunicationMethod | LinkDeliveryCommunicationMethodDict]]
    first_name: NotRequired[str]
