from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.network_status_get_response_network_status import NetworkStatusGetResponseNetworkStatusOrStr
from .network_status_get_response_layer import NetworkStatusGetResponseLayer, NetworkStatusGetResponseLayerDict


class NetworkStatusGetResponse(SdkBaseModel):
    """NetworkStatusGetResponse defines the response schema for ``/network/status/get``"""

    network_status: NetworkStatusGetResponseNetworkStatusOrStr
    """Enum representing the overall network status of the user."""

    layer: OptionalNullable[NetworkStatusGetResponseLayer] = UNSET
    """An object representing Layer-related metadata for the requested user."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class NetworkStatusGetResponseDict(TypedDict):
    network_status: NetworkStatusGetResponseNetworkStatusOrStr
    layer: NotRequired[NetworkStatusGetResponseLayer | NetworkStatusGetResponseLayerDict | None]
    request_id: str
