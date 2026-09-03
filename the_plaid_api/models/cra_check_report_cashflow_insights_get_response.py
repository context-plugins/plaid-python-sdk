from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_cashflow_insights_report import CraCashflowInsightsReport, CraCashflowInsightsReportDict
from .cra_report_warning import CraReportWarning, CraReportWarningDict


class CraCheckReportCashflowInsightsGetResponse(SdkBaseModel):
    """CraCheckReportCashflowInsightsGetResponse defines the response schema for
    ``/cra/check_report/cashflow_insights/get``."""

    report: CraCashflowInsightsReport
    """Contains data for the CRA Cashflow Insights Report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    warnings: Optional[list[CraReportWarning]] = UNSET
    """If the Cashflow Insights generation was successful but a subset of data could not be retrieved, this array will
    contain information about the errors causing information to be missing"""


class CraCheckReportCashflowInsightsGetResponseDict(TypedDict):
    report: CraCashflowInsightsReport | CraCashflowInsightsReportDict
    request_id: str
    warnings: NotRequired[list[CraReportWarning | CraReportWarningDict]]
