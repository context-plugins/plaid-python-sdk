from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gse_report_type import GseReportTypeOrStr


class CraCheckReportGseOptions(SdkBaseModel):
    """Specifies options for creating reports that can be shared with GSEs for mortgage verification."""

    report_types: list[GseReportTypeOrStr]
    """Specifies which types of reports should be made available to GSEs."""


class CraCheckReportGseOptionsDict(TypedDict):
    report_types: list[GseReportTypeOrStr]
