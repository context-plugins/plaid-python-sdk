from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkDeliveryCreateResponse(SdkBaseModel):
    """LinkDeliveryCreateResponse defines the response schema for ``/link_delivery/create``"""

    link_delivery_url: str
    """The URL to the Hosted Link session, which will be delivered by the specified delivery method."""

    link_delivery_session_id: str
    """The ID for the Hosted Link session. Same as the ``link_token`` string excluding the "link-{env}-" prefix."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class LinkDeliveryCreateResponseDict(TypedDict):
    link_delivery_url: str
    link_delivery_session_id: str
    request_id: str
