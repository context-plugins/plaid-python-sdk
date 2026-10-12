from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .category_insight_details import CategoryInsightDetails, CategoryInsightDetailsDict


class CategoryInsights(SdkBaseModel):
    """Insights on a user's top personal finance categories."""

    primary_category_insights: Optional[list[CategoryInsightDetails]] = UNSET
    """List of insights of top primary personal finance categories ranked by outflow."""

    detailed_category_insights: Optional[list[CategoryInsightDetails]] = UNSET
    """List of insights of top detailed personal finance categories ranked by outflow."""


class CategoryInsightsDict(TypedDict):
    primary_category_insights: NotRequired[list[CategoryInsightDetailsDict]]
    detailed_category_insights: NotRequired[list[CategoryInsightDetailsDict]]
