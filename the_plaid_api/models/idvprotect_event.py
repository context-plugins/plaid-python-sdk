from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .trust_index import TrustIndex, TrustIndexDict


class IdvprotectEvent(SdkBaseModel):
    """Information about a Protect event including Trust Index score and fraud attributes."""

    event_id: str
    """The event ID."""

    timestamp: RFC3339DateTime
    """The timestamp of the event, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2017-09-14T14:42:19.350Z"``"""

    trust_index: TrustIndex | None
    """Represents a calculated Trust Index Score."""

    fraud_attributes: Any | None
    """Event fraud attributes as an arbitrary set of key-value pairs. The set of attributes returned varies by model."""


class IdvprotectEventDict(TypedDict):
    event_id: str
    timestamp: RFC3339DateTime
    trust_index: TrustIndex | TrustIndexDict | None
    fraud_attributes: Any | None
