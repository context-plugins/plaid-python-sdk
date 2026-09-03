from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BusinessIndustryPredictionNullable(SdkBaseModel):
    """Nullable industry prediction details."""

    code: int
    """NAICS code for the predicted business industry."""

    title: str
    """The business industry classification of the predicted NAICS code."""


class BusinessIndustryPredictionNullableDict(TypedDict):
    code: int
    title: str
