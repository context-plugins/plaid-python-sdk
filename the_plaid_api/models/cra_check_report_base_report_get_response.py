from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .base_report import BaseReport, BaseReportDict
from .base_report_warning import BaseReportWarning, BaseReportWarningDict


class CraCheckReportBaseReportGetResponse(SdkBaseModel):
    """CraCheckReportBaseReportGetResponse defines the response schema for ``/cra/check_report/base_report/get``"""

    report: BaseReport
    """An object representing a Base Report"""

    warnings: list[BaseReportWarning]
    """This array contains any information about errors or alerts related to the Base Report that did not block
    generation of the report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CraCheckReportBaseReportGetResponseDict(TypedDict):
    report: BaseReport | BaseReportDict
    warnings: list[BaseReportWarning | BaseReportWarningDict]
    request_id: str
