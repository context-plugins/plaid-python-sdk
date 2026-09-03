from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditFreddieMacReportingInformation(SdkBaseModel):
    """Information about a report identifier and a report name."""

    report_date_time: Optional[str] = Field(default=UNSET, alias="ReportDateTime")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    report_identifier_type: Optional[str] = Field(default=UNSET, alias="ReportIdentifierType")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac. The value can only be
    "ReportID"."""

    reporting_information_parent_identifier: Optional[str] = Field(
        default=UNSET, alias="ReportingInformationParentIdentifier"
    )
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    reporting_information_identifier: str = Field(alias="ReportingInformationIdentifier")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class CreditFreddieMacReportingInformationDict(TypedDict):
    report_date_time: NotRequired[str]
    report_identifier_type: NotRequired[str]
    reporting_information_parent_identifier: NotRequired[str]
    reporting_information_identifier: str
