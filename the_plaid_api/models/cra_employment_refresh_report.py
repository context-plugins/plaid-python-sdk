from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .cra_employment_refresh_report_item import CraEmploymentRefreshReportItem, CraEmploymentRefreshReportItemDict


class CraEmploymentRefreshReport(SdkBaseModel):
    """An object representing an Employment Refresh Report."""

    generated_time: RFC3339DateTime
    """The date and time when the Employment Refresh Report was created, in ISO 8601 format (e.g.
    "2018-04-12T03:32:11Z")."""

    days_requested: float
    """The number of days of transaction history that the Employment Refresh Report covers."""

    items: list[CraEmploymentRefreshReportItem]
    """Data returned by Plaid about each of the Items included in the Employment Refresh Report."""


class CraEmploymentRefreshReportDict(TypedDict):
    generated_time: RFC3339DateTime
    days_requested: float
    items: list[CraEmploymentRefreshReportItem | CraEmploymentRefreshReportItemDict]
