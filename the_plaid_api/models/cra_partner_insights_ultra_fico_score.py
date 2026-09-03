from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CraPartnerInsightsUltraFicoScore(SdkBaseModel):
    """The calculated UltraFICO® score."""

    ultrafico_score_version: Literal["1.0"] = "1.0"
    """The version of the UltraFICO® score."""

    score: int
    """Numeric value of the UltraFICO® score."""

    negative_reason_codes: Optional[list[str]] = UNSET
    """Negative reason codes associated with the score (reasons the score moved downward), in priority order. May
    contain up to 4 items."""

    positive_reason_codes: Optional[list[str]] = UNSET
    """Positive reason codes associated with the score (reasons the score moved upward), in priority order. May contain
    up to 4 items."""

    reason_code_1: OptionalNullable[str] = UNSET
    """Deprecated. Use ``negative_reason_codes`` instead. The first reason code associated with the score."""

    reason_code_2: OptionalNullable[str] = UNSET
    """Deprecated. Use ``negative_reason_codes`` instead. The second reason code associated with the score."""

    reason_code_3: OptionalNullable[str] = UNSET
    """Deprecated. Use ``negative_reason_codes`` instead. The third reason code associated with the score."""

    reason_code_4: OptionalNullable[str] = UNSET
    """Deprecated. Use ``negative_reason_codes`` instead. The fourth reason code associated with the score."""

    positive_reason_code_1: OptionalNullable[str] = UNSET
    """Deprecated. Use ``positive_reason_codes`` instead. The first positive reason code associated with the score."""

    positive_reason_code_2: OptionalNullable[str] = UNSET
    """Deprecated. Use ``positive_reason_codes`` instead. The second positive reason code associated with the score."""

    positive_reason_code_3: OptionalNullable[str] = UNSET
    """Deprecated. Use ``positive_reason_codes`` instead. The third positive reason code associated with the score."""

    positive_reason_code_4: OptionalNullable[str] = UNSET
    """Deprecated. Use ``positive_reason_codes`` instead. The fourth positive reason code associated with the score."""

    did_inquiries_adversely_affect_score: OptionalNullable[bool] = UNSET
    """Whether inquiries adversely affected the score but were not represented in one of the four reason codes.
    Sometimes referred to as the FACTA Flag."""


class CraPartnerInsightsUltraFicoScoreDict(TypedDict):
    ultrafico_score_version: NotRequired[Literal["1.0"]]
    score: int
    negative_reason_codes: NotRequired[list[str]]
    positive_reason_codes: NotRequired[list[str]]
    reason_code_1: NotRequired[str | None]
    reason_code_2: NotRequired[str | None]
    reason_code_3: NotRequired[str | None]
    reason_code_4: NotRequired[str | None]
    positive_reason_code_1: NotRequired[str | None]
    positive_reason_code_2: NotRequired[str | None]
    positive_reason_code_3: NotRequired[str | None]
    positive_reason_code_4: NotRequired[str | None]
    did_inquiries_adversely_affect_score: NotRequired[bool | None]
