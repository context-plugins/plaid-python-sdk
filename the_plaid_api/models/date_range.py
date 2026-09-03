from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class DateRange(SdkBaseModel):
    """A date range with a start and end date"""

    beginning: Date
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    ending: Date
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""


class DateRangeDict(TypedDict):
    beginning: Date
    ending: Date
