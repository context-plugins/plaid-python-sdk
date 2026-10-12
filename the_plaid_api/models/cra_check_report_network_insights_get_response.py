from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_network_insights_report import CraNetworkInsightsReport, CraNetworkInsightsReportDict
from .cra_report_warning import CraReportWarning, CraReportWarningDict


class CraCheckReportNetworkInsightsGetResponse(SdkBaseModel):
    """CraCheckReportNetworkInsightsGetResponse defines the response schema for
    ``/cra/check_report/network_insights/get``."""

    report: CraNetworkInsightsReport
    """Contains data for the CRA Network Attributes Report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    warnings: Optional[list[CraReportWarning]] = UNSET
    """If the Network Insights generation was successful but a subset of data could not be retrieved, this array will
    contain information about the errors causing information to be missing"""


class CraCheckReportNetworkInsightsGetResponseDict(TypedDict):
    report: CraNetworkInsightsReportDict
    request_id: str
    warnings: NotRequired[list[CraReportWarningDict]]
