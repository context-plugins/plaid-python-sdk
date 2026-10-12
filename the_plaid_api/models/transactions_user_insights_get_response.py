from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .category_insights import CategoryInsights, CategoryInsightsDict
from .counterparty_insights import CounterpartyInsights, CounterpartyInsightsDict
from .recurring_transactions import RecurringTransactions, RecurringTransactionsDict
from .user_data_overview import UserDataOverview, UserDataOverviewDict


class TransactionsUserInsightsGetResponse(SdkBaseModel):
    """TransactionsUserInsightsGetResponse defines the response schema for
    ``/beta/transactions/user_insights/v1/get``."""

    user_data_overview: UserDataOverview
    """metadata for the set of insights provided in ``TransactionsUserInsightsGetResponse``"""

    counterparty_insights: Optional[CounterpartyInsights] = UNSET
    """Insights around a user's counterparties"""

    category_insights: Optional[CategoryInsights] = UNSET
    """Insights on a user's top personal finance categories."""

    recurring_transactions: Optional[RecurringTransactions] = UNSET
    """Insights object for recurring transactions for ``/beta/transactions/user_insights/v1/get`` endpoint"""


class TransactionsUserInsightsGetResponseDict(TypedDict):
    user_data_overview: UserDataOverviewDict
    counterparty_insights: NotRequired[CounterpartyInsightsDict]
    category_insights: NotRequired[CategoryInsightsDict]
    recurring_transactions: NotRequired[RecurringTransactionsDict]
