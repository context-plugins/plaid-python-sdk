from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenTransactions(SdkBaseModel):
    """Configuration parameters for the Transactions product"""

    days_requested: Optional[int] = UNSET
    """The maximum number of days of transaction history to request for the Transactions product. The more transaction
    history is requested, the longer the historical update poll will take. The default value is 90 days. In Production,
    if a value under 30 is provided, a minimum of 30 days of history will be requested. Once Transactions has been added
    to an Item, this value cannot be updated.

    Customers using `Recurring Transactions
    <https://plaid.com/docs/api/products/transactions/#transactionsrecurringget>`__ should request at least 180 days of
    history for optimal results."""


class LinkTokenTransactionsDict(TypedDict):
    days_requested: NotRequired[int]
