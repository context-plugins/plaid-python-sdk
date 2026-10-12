from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .cra_check_report_create_employment_refresh_options import (
    CraCheckReportCreateEmploymentRefreshOptions,
    CraCheckReportCreateEmploymentRefreshOptionsDict,
)
from .enums.cra_check_report_verification_get_report_type import CraCheckReportVerificationGetReportTypeOrStr


class CraCheckReportHomeLendingReportOptions(SdkBaseModel):
    """Options for configuring Home Lending Report (Verification Report) generation."""

    reports_requested: list[CraCheckReportVerificationGetReportTypeOrStr]
    """Specifies which types of home lending reports to generate."""

    employment_refresh_options: OptionalNullable[CraCheckReportCreateEmploymentRefreshOptions] = UNSET
    """Defines configuration options for the Employment Refresh Report."""


class CraCheckReportHomeLendingReportOptionsDict(TypedDict):
    reports_requested: list[CraCheckReportVerificationGetReportTypeOrStr]
    employment_refresh_options: NotRequired[CraCheckReportCreateEmploymentRefreshOptionsDict | None]
