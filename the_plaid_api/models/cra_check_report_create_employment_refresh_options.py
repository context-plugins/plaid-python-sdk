from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraCheckReportCreateEmploymentRefreshOptions(SdkBaseModel):
    """Defines configuration options for the Employment Refresh Report."""

    days_requested: int
    """The number of days of data to request for the report. This field is required if an Employment Refresh Report is
    requested. Maximum is 731."""


class CraCheckReportCreateEmploymentRefreshOptionsDict(TypedDict):
    days_requested: int
