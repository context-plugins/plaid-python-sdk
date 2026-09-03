from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .link_event_metadata import LinkEventMetadata, LinkEventMetadataDict


class LinkEvent(SdkBaseModel):
    """An event that occurred while the user was going through Link"""

    event_name: str
    """Event name"""

    timestamp: str
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    event_id: str
    """UUID that can be used to deduplicate events"""

    event_metadata: LinkEventMetadata
    """Metadata about an event that occurred while the user was going through Link"""


class LinkEventDict(TypedDict):
    event_name: str
    timestamp: str
    event_id: str
    event_metadata: LinkEventMetadata | LinkEventMetadataDict
