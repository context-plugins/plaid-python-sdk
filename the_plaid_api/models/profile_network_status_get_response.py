from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.network_status_get_response_network_status import NetworkStatusGetResponseNetworkStatusOrStr


class ProfileNetworkStatusGetResponse(SdkBaseModel):
    """ProfileNetworkStatusGetResponse defines the response schema for ``/profile/network_status/get``"""

    network_status: NetworkStatusGetResponseNetworkStatusOrStr
    """Enum representing the overall network status of the user."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProfileNetworkStatusGetResponseDict(TypedDict):
    network_status: NetworkStatusGetResponseNetworkStatusOrStr
    request_id: str
