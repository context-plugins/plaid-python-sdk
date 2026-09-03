from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.cra_partner_insights_base_fico_score_version import CraPartnerInsightsBaseFicoScoreVersionOrStr
from .enums.cra_partner_insights_bureau import CraPartnerInsightsBureauOrStr


class CraPartnerInsightsBaseFicoScore(SdkBaseModel):
    """Details about the base FICO score associated with an UltraFICO® scoring request."""

    bureau: CraPartnerInsightsBureauOrStr
    """The credit bureau that provided the base FICO score."""

    score: int
    """Numeric value of the base FICO score."""

    reason_codes: Optional[list[str]] = UNSET
    """Reason codes associated with the score, in priority order. May contain up to 4 items."""

    reason_code_1: OptionalNullable[str] = UNSET
    """Deprecated. Use ``reason_codes`` instead. The first reason code associated with the score."""

    reason_code_2: OptionalNullable[str] = UNSET
    """Deprecated. Use ``reason_codes`` instead. The second reason code associated with the score."""

    reason_code_3: OptionalNullable[str] = UNSET
    """Deprecated. Use ``reason_codes`` instead. The third reason code associated with the score."""

    reason_code_4: OptionalNullable[str] = UNSET
    """Deprecated. Use ``reason_codes`` instead. The fourth reason code associated with the score."""

    did_inquiries_adversely_affect_score: OptionalNullable[bool] = UNSET
    """Whether inquiries adversely affected the score but were not represented in one of the four reason codes.
    Sometimes referred to as the FACTA Flag."""

    base_fico_score_version: CraPartnerInsightsBaseFicoScoreVersionOrStr
    """The version of the base FICO score model."""


class CraPartnerInsightsBaseFicoScoreDict(TypedDict):
    bureau: CraPartnerInsightsBureauOrStr
    score: int
    reason_codes: NotRequired[list[str]]
    reason_code_1: NotRequired[str | None]
    reason_code_2: NotRequired[str | None]
    reason_code_3: NotRequired[str | None]
    reason_code_4: NotRequired[str | None]
    did_inquiries_adversely_affect_score: NotRequired[bool | None]
    base_fico_score_version: CraPartnerInsightsBaseFicoScoreVersionOrStr
