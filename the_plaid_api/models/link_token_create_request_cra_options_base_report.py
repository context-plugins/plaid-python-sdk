from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .cra_check_report_home_lending_report_options import (
    CraCheckReportHomeLendingReportOptions,
    CraCheckReportHomeLendingReportOptionsDict,
)
from .link_token_create_request_cra_options_base_report_gseoptions import (
    LinkTokenCreateRequestCraOptionsBaseReportGseoptions,
    LinkTokenCreateRequestCraOptionsBaseReportGseoptionsDict,
)


class LinkTokenCreateRequestCraOptionsBaseReport(SdkBaseModel):
    """Specifies options for initializing Link for use with the Base Report product, specifically the
    ``client_report_id``."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    gse_options: OptionalNullable[LinkTokenCreateRequestCraOptionsBaseReportGseoptions] = UNSET
    """Specifies options for initializing Link to create reports that can be shared with GSEs for mortgage
    verification."""

    require_identity: OptionalNullable[bool] = UNSET
    """Indicates that the report must include identity information. If identity information is not available, the report
    will fail."""

    home_lending_report_options: OptionalNullable[CraCheckReportHomeLendingReportOptions] = UNSET
    """Options for configuring Home Lending Report (Verification Report) generation."""


class LinkTokenCreateRequestCraOptionsBaseReportDict(TypedDict):
    client_report_id: NotRequired[str | None]
    gse_options: NotRequired[LinkTokenCreateRequestCraOptionsBaseReportGseoptionsDict | None]
    require_identity: NotRequired[bool | None]
    home_lending_report_options: NotRequired[CraCheckReportHomeLendingReportOptionsDict | None]
