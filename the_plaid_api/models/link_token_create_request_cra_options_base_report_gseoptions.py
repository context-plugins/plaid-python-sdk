from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gsereport_type import GsereportTypeOrStr


class LinkTokenCreateRequestCraOptionsBaseReportGseoptions(SdkBaseModel):
    """Specifies options for initializing Link to create reports that can be shared with GSEs for mortgage
    verification."""

    report_types: list[GsereportTypeOrStr]
    """Specifies which types of reports should be made available to GSEs."""


class LinkTokenCreateRequestCraOptionsBaseReportGseoptionsDict(TypedDict):
    report_types: list[GsereportTypeOrStr]
