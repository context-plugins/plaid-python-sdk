from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prism_cash_score_metadata import PrismCashScoreMetadata, PrismCashScoreMetadataDict


class PrismFirstDetect(SdkBaseModel):
    """The data from the FirstDetect product returned by Prism Data."""

    version: int
    """The version of Prism Data's FirstDetect model used. This field is deprecated in favor of ``model_version``."""

    model_version: Optional[str] = UNSET
    """The version of Prism Data's FirstDetect model used."""

    score: int | None
    """The score returned by Prism Data. Ranges from 1-999, with higher score indicating lower risk."""

    reason_codes: Optional[list[str]] = UNSET
    """The reasons for an individual having risk according to the FirstDetect score."""

    metadata: Optional[PrismCashScoreMetadata] = UNSET
    """An object containing metadata about the provided transactions."""

    error_reason: Optional[str] = UNSET
    """The error returned by Prism for this product."""


class PrismFirstDetectDict(TypedDict):
    version: int
    model_version: NotRequired[str]
    score: int | None
    reason_codes: NotRequired[list[str]]
    metadata: NotRequired[PrismCashScoreMetadata | PrismCashScoreMetadataDict]
    error_reason: NotRequired[str]
