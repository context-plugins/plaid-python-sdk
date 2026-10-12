from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .institution_supported_networks import InstitutionSupportedNetworks, InstitutionSupportedNetworksDict


class TransferCapabilitiesGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/capabilities/get``"""

    institution_supported_networks: InstitutionSupportedNetworks
    """Contains the RTP and RfP network and types supported by the linked Item's institution."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferCapabilitiesGetResponseDict(TypedDict):
    institution_supported_networks: InstitutionSupportedNetworksDict
    request_id: str
