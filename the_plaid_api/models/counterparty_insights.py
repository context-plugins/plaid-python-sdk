from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .financial_institution_insights import FinancialInstitutionInsights, FinancialInstitutionInsightsDict
from .merchant_insights import MerchantInsights, MerchantInsightsDict


class CounterpartyInsights(SdkBaseModel):
    """Insights around a user's counterparties"""

    financial_institution_insights: Optional[list[FinancialInstitutionInsights]] = UNSET
    """Insights related to a user's transactions with other financial institutions, including detected account types."""

    merchant_insights: Optional[list[MerchantInsights]] = UNSET
    """Insights about a user's top merchants, ranked by spend."""


class CounterpartyInsightsDict(TypedDict):
    financial_institution_insights: NotRequired[list[FinancialInstitutionInsights | FinancialInstitutionInsightsDict]]
    merchant_insights: NotRequired[list[MerchantInsights | MerchantInsightsDict]]
