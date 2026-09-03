from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_partner_insights_base_fico_score import CraPartnerInsightsBaseFicoScore, CraPartnerInsightsBaseFicoScoreDict


class CraPartnerInsightsUltraFicoScoreRequest(SdkBaseModel):
    """Configuration required to generate a single UltraFICO® score."""

    ultrafico_score_version: Literal["1.0"] = "1.0"
    """The version of the UltraFICO® score."""

    fico_scoring_request_id: Optional[str] = UNSET
    """FICO identifier for a particular scoring request. Should only be provided by FICO as part of the FICO-led
    flow."""

    request_correlation_id: Optional[str] = UNSET
    """Client-generated identifier that can be used to correlate scoring requests with their scoring results."""

    base_fico_score: CraPartnerInsightsBaseFicoScore
    """Details about the base FICO score associated with an UltraFICO® scoring request."""


class CraPartnerInsightsUltraFicoScoreRequestDict(TypedDict):
    ultrafico_score_version: NotRequired[Literal["1.0"]]
    fico_scoring_request_id: NotRequired[str]
    request_correlation_id: NotRequired[str]
    base_fico_score: CraPartnerInsightsBaseFicoScore | CraPartnerInsightsBaseFicoScoreDict
