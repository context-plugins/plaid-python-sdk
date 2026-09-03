from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CategoryInsightDetails(SdkBaseModel):
    """Insights object for categories."""

    name: str
    """Category name."""

    transaction_count: int
    """The number of transactions associated with this category."""

    total_outflows: float
    """Sum of outflow amounts."""

    total_inflows: float
    """Sum of inflow amounts."""

    top_counterparties: Optional[list[str]] = UNSET
    """The most common counterparties associated with this category sorted by outflow."""


class CategoryInsightDetailsDict(TypedDict):
    name: str
    transaction_count: int
    total_outflows: float
    total_inflows: float
    top_counterparties: NotRequired[list[str]]
