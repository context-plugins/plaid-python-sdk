from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class LendScore(SdkBaseModel):
    """The results of the LendScore"""

    score: OptionalNullable[int] = UNSET
    """The score returned by the LendScore model. Will be an integer in the range 1 to 99. Higher scores indicate lower
    credit risk."""

    reason_codes: Optional[list[str]] = UNSET
    """The reasons for an individual having risk according to the LendScore. For a full list of possible reason codes
    and a mapping of reason codes to human-readable reasons, contact your Plaid account manager. Different LendScore
    versions will use different sets of reason codes."""

    error_reason: OptionalNullable[str] = UNSET
    """Human-readable description of why the LendScore could not be computed."""


class LendScoreDict(TypedDict):
    score: NotRequired[int | None]
    reason_codes: NotRequired[list[str]]
    error_reason: NotRequired[str | None]
