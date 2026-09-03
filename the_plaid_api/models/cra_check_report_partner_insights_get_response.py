from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_partner_insights import CraPartnerInsights, CraPartnerInsightsDict
from .cra_report_warning import CraReportWarning, CraReportWarningDict


class CraCheckReportPartnerInsightsGetResponse(SdkBaseModel):
    """CraCheckReportPartnerInsightsGetResponse defines the response schema for
    ``/cra/check_report/partner_insights/get``."""

    report: Optional[CraPartnerInsights] = UNSET
    """The Partner Insights report of the bank data for an end user."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    warnings: Optional[list[CraReportWarning]] = UNSET
    """If the Partner Insights generation was successful but a subset of data could not be retrieved, this array will
    contain information about the errors causing information to be missing"""


class CraCheckReportPartnerInsightsGetResponseDict(TypedDict):
    report: NotRequired[CraPartnerInsights | CraPartnerInsightsDict]
    request_id: str
    warnings: NotRequired[list[CraReportWarning | CraReportWarningDict]]
