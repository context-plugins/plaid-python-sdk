from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cra_partner_insights_ultra_fico_score import (
    CraPartnerInsightsUltraFicoScore,
    CraPartnerInsightsUltraFicoScoreDict,
)


class CraPartnerInsightsUltraFicoScoreResult(SdkBaseModel):
    """The result of a single UltraFICO® score generation request."""

    request_correlation_id: Optional[str] = UNSET
    """Client-generated identifier that can be used to correlate scoring requests with their scoring results."""

    fico_scoring_request_id: Optional[str] = UNSET
    """FICO-provided identifier that uniquely identifies this score generation request."""

    ultrafico_score: OptionalNullable[CraPartnerInsightsUltraFicoScore] = UNSET
    """The calculated UltraFICO® score."""

    error_reason: Optional[str] = UNSET
    """Human-readable description of why the UltraFICO® score could not be computed."""

    exclusion_code: OptionalNullable[str] = UNSET
    """FICO exclusion code indicating why an UltraFICO® score could not be computed due to consumer-data conditions
    (e.g. insufficient account history). ``null`` when the exclusion code is not set; "0" when a score was produced."""


class CraPartnerInsightsUltraFicoScoreResultDict(TypedDict):
    request_correlation_id: NotRequired[str]
    fico_scoring_request_id: NotRequired[str]
    ultrafico_score: NotRequired[CraPartnerInsightsUltraFicoScoreDict | None]
    error_reason: NotRequired[str]
    exclusion_code: NotRequired[str | None]
