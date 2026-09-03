from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.link_delivery_webhook_callback_type import LinkDeliveryWebhookCallbackTypeOrStr
from .enums.link_event_name import LinkEventNameOrStr
from .link_delivery_account import LinkDeliveryAccount, LinkDeliveryAccountDict
from .link_delivery_institution import LinkDeliveryInstitution, LinkDeliveryInstitutionDict


class LinkCallbackMetadata(SdkBaseModel):
    """Information related to the callback from the Hosted Link session."""

    callback_type: Optional[LinkDeliveryWebhookCallbackTypeOrStr] = UNSET
    """The type of Link callback event"""

    event_name: Optional[LinkEventNameOrStr] = UNSET
    """A string representing the event that has just occurred in the Link flow."""

    status: Optional[str] = UNSET
    """Indicates where in the flow the Link user exited"""

    link_session_id: Optional[str] = UNSET
    """A unique identifier associated with a user's actions and events through the Link flow. Include this identifier
    when opening a support ticket for faster turnaround."""

    request_id: Optional[str] = UNSET
    """The request ID for the last request made by Link. This can be shared with Plaid support to expedite
    investigation."""

    institution: Optional[LinkDeliveryInstitution] = UNSET
    """Information related to the financial institution."""

    accounts: Optional[list[LinkDeliveryAccount]] = UNSET
    """A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard,
    accounts will only include selected accounts."""


class LinkCallbackMetadataDict(TypedDict):
    callback_type: NotRequired[LinkDeliveryWebhookCallbackTypeOrStr]
    event_name: NotRequired[LinkEventNameOrStr]
    status: NotRequired[str]
    link_session_id: NotRequired[str]
    request_id: NotRequired[str]
    institution: NotRequired[LinkDeliveryInstitution | LinkDeliveryInstitutionDict]
    accounts: NotRequired[list[LinkDeliveryAccount | LinkDeliveryAccountDict]]
