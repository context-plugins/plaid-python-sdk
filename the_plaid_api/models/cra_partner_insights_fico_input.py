from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_partner_insights_ultra_fico_score_request import (
    CraPartnerInsightsUltraFicoScoreRequest,
    CraPartnerInsightsUltraFicoScoreRequestDict,
)


class CraPartnerInsightsFicoInput(SdkBaseModel):
    """Configuration for the FICO products used in the Partner Insights product."""

    fico_lender_id: str
    """ID provided by FICO that uniquely identifies the lender. Required for UltraFICO® score generation. Sometimes
    referred to as Lender Org ID."""

    lender_application_id: str
    """Client-generated identifier that uniquely identifies the FICO Application across FICO systems."""

    ultrafico_score_requests: list[CraPartnerInsightsUltraFicoScoreRequest]
    """A list of UltraFICO® scoring requests. Each request contains all configuration required to generate an UltraFICO
    score."""


class CraPartnerInsightsFicoInputDict(TypedDict):
    fico_lender_id: str
    lender_application_id: str
    ultrafico_score_requests: list[
        CraPartnerInsightsUltraFicoScoreRequest | CraPartnerInsightsUltraFicoScoreRequestDict
    ]
