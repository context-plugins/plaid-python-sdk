from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.hosted_link_delivery_method import HostedLinkDeliveryMethodOrStr


class LinkTokenCreateHostedLink(SdkBaseModel):
    """Configuration parameters for Hosted Link. To enable the session for Hosted Link, send this object in the request.
    It can be empty."""

    delivery_method: Optional[HostedLinkDeliveryMethodOrStr] = UNSET
    """How Plaid should deliver the Plaid Link session to the customer. Only available to customers enabled for Link
    Delivery (beta). To request Link Delivery access, contact your account manager. 'sms' will deliver via SMS. Must
    pass ``user.phone_number``. 'email' will deliver via email. Must pass ``user.email_address``. In the Sandbox
    environment, this field will be ignored; use the Production environment to test Link Delivery instead."""

    completion_redirect_uri: Optional[str] = UNSET
    """URI that Hosted Link will redirect to upon completion of the Link flow. This will only occur in Hosted Link
    sessions, not in other implementation methods."""

    url_lifetime_seconds: Optional[int] = UNSET
    """How many seconds the link will be valid for. Must be positive. Cannot be longer than 21 days. The default
    lifetime is 7 days for links delivered by email, 1 day for links delivered via SMS, and 30 minutes for links not
    sent via Plaid Link delivery. This parameter will override the value of all three link types."""

    is_mobile_app: bool = False
    """This indicates whether the client is opening Hosted Link in a mobile app in an ``AsWebAuthenticationSession`` or
    Chrome custom tab."""


class LinkTokenCreateHostedLinkDict(TypedDict):
    delivery_method: NotRequired[HostedLinkDeliveryMethodOrStr]
    completion_redirect_uri: NotRequired[str]
    url_lifetime_seconds: NotRequired[int]
    is_mobile_app: NotRequired[bool]
