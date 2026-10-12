from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .cra_check_report_gseoptions import CraCheckReportGseoptions, CraCheckReportGseoptionsDict
from .cra_check_report_home_lending_report_options import (
    CraCheckReportHomeLendingReportOptions,
    CraCheckReportHomeLendingReportOptionsDict,
)


class CraCheckReportCreateBaseReportOptions(SdkBaseModel):
    """Defines configuration options to generate a Base Report"""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications. This field is deprecated.
    Use the ``client_report_id`` field at the top level of the request instead."""

    gse_options: OptionalNullable[CraCheckReportGseoptions] = UNSET
    """Specifies options for creating reports that can be shared with GSEs for mortgage verification."""

    require_identity: OptionalNullable[bool] = UNSET
    """Indicates that the report must include identity information. If identity information is not available, the report
    will fail."""

    home_lending_report_options: OptionalNullable[CraCheckReportHomeLendingReportOptions] = UNSET
    """Options for configuring Home Lending Report (Verification Report) generation."""


class CraCheckReportCreateBaseReportOptionsDict(TypedDict):
    client_report_id: NotRequired[str | None]
    gse_options: NotRequired[CraCheckReportGseoptionsDict | None]
    require_identity: NotRequired[bool | None]
    home_lending_report_options: NotRequired[CraCheckReportHomeLendingReportOptionsDict | None]
