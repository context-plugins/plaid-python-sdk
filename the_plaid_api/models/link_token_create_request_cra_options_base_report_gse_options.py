from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gse_report_type import GseReportTypeOrStr


class LinkTokenCreateRequestCraOptionsBaseReportGseOptions(SdkBaseModel):
    """Specifies options for initializing Link to create reports that can be shared with GSEs for mortgage
    verification."""

    report_types: list[GseReportTypeOrStr]
    """Specifies which types of reports should be made available to GSEs."""


class LinkTokenCreateRequestCraOptionsBaseReportGseOptionsDict(TypedDict):
    report_types: list[GseReportTypeOrStr]
