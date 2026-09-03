from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .cra_partner_insights_fico_report_characteristics import (
    CraPartnerInsightsFicoReportCharacteristics,
    CraPartnerInsightsFicoReportCharacteristicsDict,
)
from .cra_partner_insights_ultra_fico_score_result import (
    CraPartnerInsightsUltraFicoScoreResult,
    CraPartnerInsightsUltraFicoScoreResultDict,
)


class CraPartnerInsightsFicoResults(SdkBaseModel):
    """The calculated UltraFICO® scores returned as part of the Partner Insights report."""

    lender_application_id: str
    """Client-generated identifier that uniquely identifies the FICO Application across FICO systems."""

    ultrafico_score_results: list[CraPartnerInsightsUltraFicoScoreResult]
    """UltraFICO® scoring results, one per provided UltraFICO scoring request."""

    report_characteristics: OptionalNullable[CraPartnerInsightsFicoReportCharacteristics] = UNSET
    """Report characteristics returned by FICO describing the banking data used to generate the UltraFICO® score."""


class CraPartnerInsightsFicoResultsDict(TypedDict):
    lender_application_id: str
    ultrafico_score_results: list[CraPartnerInsightsUltraFicoScoreResult | CraPartnerInsightsUltraFicoScoreResultDict]
    report_characteristics: NotRequired[
        CraPartnerInsightsFicoReportCharacteristics | CraPartnerInsightsFicoReportCharacteristicsDict | None
    ]
