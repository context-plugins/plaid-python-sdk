from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_capabilities_get_rf_p import TransferCapabilitiesGetRfP, TransferCapabilitiesGetRfPDict
from .transfer_capabilities_get_rtp import TransferCapabilitiesGetRtp, TransferCapabilitiesGetRtpDict


class InstitutionSupportedNetworks(SdkBaseModel):
    """Contains the RTP and RfP network and types supported by the linked Item's institution."""

    rtp: TransferCapabilitiesGetRtp
    """Contains the supported service types in RTP"""

    rfp: TransferCapabilitiesGetRfP
    """Contains the supported service types in RfP"""


class InstitutionSupportedNetworksDict(TypedDict):
    rtp: TransferCapabilitiesGetRtpDict
    rfp: TransferCapabilitiesGetRfPDict
