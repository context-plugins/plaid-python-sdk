from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .expenditure_insights import ExpenditureInsights, ExpenditureInsightsDict
from .income_insights import IncomeInsights, IncomeInsightsDict


class AffordabilityInsights(SdkBaseModel):
    """Affordability insights focus on providing signal on the ability of a borrower to repay their loan without
    experiencing financial strain. It provides insights on factors such as a user's monthly income and expenses,
    disposable income, average expenditure, etc., helping lenders gauge the level of affordability of a borrower."""

    expenditure: OptionalNullable[ExpenditureInsights] = UNSET
    """Comprehensive analysis of spending patterns, categorizing expenses into essential, non-essential, and other
    categories."""

    income: OptionalNullable[IncomeInsights] = UNSET
    """Comprehensive income analysis including total income, income excluding transfers, and inbound transfer
    amounts."""


class AffordabilityInsightsDict(TypedDict):
    expenditure: NotRequired[ExpenditureInsightsDict | None]
    income: NotRequired[IncomeInsightsDict | None]
