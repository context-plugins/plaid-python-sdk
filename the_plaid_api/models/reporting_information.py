from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReportingInformation(SdkBaseModel):
    """Information about a report identifier and a report name."""

    reporting_information_identifier: str = Field(alias="ReportingInformationIdentifier")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class ReportingInformationDict(TypedDict):
    reporting_information_identifier: str
