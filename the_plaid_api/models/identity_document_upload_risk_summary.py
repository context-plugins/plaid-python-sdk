from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class IdentityDocumentUploadRiskSummary(SdkBaseModel):
    """Risk summary of an uploaded document."""

    risk_score: OptionalNullable[int] = UNSET
    """A number between 0 and 100, inclusive, where a score closer to 0 indicates a document is likely to be trustworthy
    and a score closer to 100 indicates a document is likely to be fraudulent."""


class IdentityDocumentUploadRiskSummaryDict(TypedDict):
    risk_score: NotRequired[int | None]
