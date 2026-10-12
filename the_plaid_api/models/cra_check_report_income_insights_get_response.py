from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_income_insights import CraIncomeInsights, CraIncomeInsightsDict
from .cra_report_warning import CraReportWarning, CraReportWarningDict


class CraCheckReportIncomeInsightsGetResponse(SdkBaseModel):
    """CraCheckReportIncomeInsightsGetResponse defines the response schema for
    ``/cra/check_report/income_insights/get``."""

    report: Optional[CraIncomeInsights] = UNSET
    """The Check Income Insights Report for an end user."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    warnings: Optional[list[CraReportWarning]] = UNSET
    """If the Income Insights generation was successful but a subset of data could not be retrieved, this array will
    contain information about the errors causing information to be missing"""


class CraCheckReportIncomeInsightsGetResponseDict(TypedDict):
    report: NotRequired[CraIncomeInsightsDict]
    request_id: str
    warnings: NotRequired[list[CraReportWarningDict]]
