from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BusinessIndustryPrediction(SdkBaseModel):
    """The predicted industry classification for the business, based on digital presence assessments."""

    code: int
    """NAICS code for the predicted business industry."""

    title: str
    """The business industry classification of the predicted NAICS code."""


class BusinessIndustryPredictionDict(TypedDict):
    code: int
    title: str
