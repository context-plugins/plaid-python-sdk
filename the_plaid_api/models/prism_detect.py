from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prism_cash_score_metadata import PrismCashScoreMetadata, PrismCashScoreMetadataDict


class PrismDetect(SdkBaseModel):
    """The data from the CashScore® Detect product returned by Prism Data."""

    model_version: str
    """The version of Prism Data's CashScore® Detect model used."""

    score: int | None
    """The score returned by Prism Data. Ranges from 1-999, with higher score indicating lower risk."""

    reason_codes: Optional[list[str]] = UNSET
    """The reasons for an individual having risk according to the CashScore® Detect score."""

    metadata: Optional[PrismCashScoreMetadata] = UNSET
    """An object containing metadata about the provided transactions."""

    error_reason: Optional[str] = UNSET
    """The error returned by Prism for this product."""


class PrismDetectDict(TypedDict):
    model_version: str
    score: int | None
    reason_codes: NotRequired[list[str]]
    metadata: NotRequired[PrismCashScoreMetadataDict]
    error_reason: NotRequired[str]
