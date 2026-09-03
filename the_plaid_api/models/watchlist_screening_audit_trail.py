from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.source import SourceOrStr


class WatchlistScreeningAuditTrail(SdkBaseModel):
    """Information about the last change made to the parent object specifying what caused the change as well as when it
    occurred."""

    source: SourceOrStr
    """A type indicating who or what last touched this object. ``dashboard``, ``link``, and ``api`` indicate the
    originating surface; ``system`` indicates Plaid. ``retro`` indicates a screening created retroactively via a bulk
    screening creation."""

    dashboard_user_id: str | None
    """ID of the associated user. To retrieve the email address or other details of the person corresponding to this ID,
    use ``/dashboard_user/get``."""

    timestamp: RFC3339DateTime
    """An ISO8601 formatted timestamp."""


class WatchlistScreeningAuditTrailDict(TypedDict):
    source: SourceOrStr
    dashboard_user_id: str | None
    timestamp: RFC3339DateTime
