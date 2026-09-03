from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class UserAccountSessionEvent(SdkBaseModel):
    """Event data for user account session tracking"""

    name: str
    """The name of the event."""

    timestamp: RFC3339DateTime
    """The timestamp when the event occurred in ISO 8601 format."""

    outcome: Optional[str] = UNSET
    """Optional outcome of the event."""


class UserAccountSessionEventDict(TypedDict):
    name: str
    timestamp: RFC3339DateTime
    outcome: NotRequired[str]
