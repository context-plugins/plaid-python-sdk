from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraCheckReportVerificationGetEmploymentRefreshOptions(SdkBaseModel):
    """Deprecated. This field is no longer accepted for new clients (created on or after 2026-07-01). New clients should
    specify required products when creating the Consumer Report. Existing integrations may continue to pass
    ``employment_refresh_options``."""

    days_requested: int
    """The number of days of data to request for the report. This field is required if an Employment Refresh Report is
    requested. Maximum is 731."""


class CraCheckReportVerificationGetEmploymentRefreshOptionsDict(TypedDict):
    days_requested: int
