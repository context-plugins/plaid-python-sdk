from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraCreditProfileLendScore(SdkBaseModel):
    """An individual LendScore result within a credit profile report."""

    score: int | None
    """The score returned by the LendScore model. Will be an integer in the range 1 to 99. Higher scores indicate lower
    credit risk."""

    reason_codes: list[str]
    """The reasons for an individual having risk according to the LendScore. For a full list of possible reason codes
    and a mapping of reason codes to human-readable reasons, contact your Plaid account manager. Different LendScore
    versions will use different sets of reason codes."""

    variant: str
    """The variant identifier for this LendScore result."""

    error_reason: str | None
    """Human-readable description of why the LendScore could not be computed."""


class CraCreditProfileLendScoreDict(TypedDict):
    score: int | None
    reason_codes: list[str]
    variant: str
    error_reason: str | None
