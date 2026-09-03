from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class TosacceptanceMetadata(SdkBaseModel):
    """Metadata related to the acceptance of Terms of Service"""

    agreement_accepted: bool
    """Indicates whether the TOS agreement was accepted"""

    originator_ip_address: str
    """The IP address of the originator when they accepted the TOS. Formatted as an IPv4 or IPv6 IP address"""

    agreement_accepted_at: RFC3339DateTime
    """ISO8601 timestamp indicating when the originator accepted the TOS"""


class TosacceptanceMetadataDict(TypedDict):
    agreement_accepted: bool
    originator_ip_address: str
    agreement_accepted_at: RFC3339DateTime
