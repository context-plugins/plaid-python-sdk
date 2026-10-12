from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .affordability_insights import AffordabilityInsights, AffordabilityInsightsDict
from .risk_indicators import RiskIndicators, RiskIndicatorsDict


class AccountInsights(SdkBaseModel):
    """This is a container object for all lending-related insights. This field will be returned only for European
    customers."""

    risk: OptionalNullable[RiskIndicators] = UNSET
    """Risk indicators focus on providing signal on the possibility of a borrower defaulting on their loan repayments by
    providing data points related to its payment behavior, debt, and other relevant financial information, helping
    lenders gauge the level of risk involved in a certain operation."""

    affordability: OptionalNullable[AffordabilityInsights] = UNSET
    """Affordability insights focus on providing signal on the ability of a borrower to repay their loan without
    experiencing financial strain. It provides insights on factors such as a user's monthly income and expenses,
    disposable income, average expenditure, etc., helping lenders gauge the level of affordability of a borrower."""


class AccountInsightsDict(TypedDict):
    risk: NotRequired[RiskIndicatorsDict | None]
    affordability: NotRequired[AffordabilityInsightsDict | None]
