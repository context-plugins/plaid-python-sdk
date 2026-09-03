from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MerchantInsights(SdkBaseModel):
    """Insights into a user's top merchants."""

    name: str
    """The counterparty name."""

    entity_id: OptionalNullable[str] = UNSET
    """A unique, stable, Plaid-generated id that maps to the merchant."""

    website: str | None
    """The website associated with the merchant."""

    transaction_count: int
    """The number of transactions associated with merchant of this type."""

    personal_finance_category_primary: str | None
    """The primary personal finance category associated with this merchant."""

    personal_finance_category_detailed: str | None
    """The detailed personal finance category associated with this merchant."""

    total_outflows: float
    """Sum of outflow amounts."""

    total_inflows: float
    """Sum of inflow amounts."""


class MerchantInsightsDict(TypedDict):
    name: str
    entity_id: NotRequired[str | None]
    website: str | None
    transaction_count: int
    personal_finance_category_primary: str | None
    personal_finance_category_detailed: str | None
    total_outflows: float
    total_inflows: float
