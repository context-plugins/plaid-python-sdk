from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class DetectedAccount(SdkBaseModel):
    """A possible account detected to be associated with a transaction user."""

    account_type: str | None
    """The detected account type (depository, credit, loan, investment etc.)."""

    account_subtype: str | None
    """The detected subtype of the account, based on the transactions to/from the institution."""

    transaction_count: int
    """The number of transactions associated with this detected account type at this financial institution."""

    oldest_transaction_date: Optional[Date] = UNSET
    """The date of the oldest transaction associated with this detected account type at this financial institution."""

    newest_transaction_date: Optional[Date] = UNSET
    """The date of the newest transaction associated with this detected account type at this financial institution."""

    newest_transaction_amount: Optional[float] = UNSET
    """Amount of the most recent transaction associated with this detected account type at this financial
    institution."""

    total_outflows: float
    """Sum of outflow amounts associated with this detected account type at this financial institution."""

    total_inflows: float
    """Sum of inflow amounts associated with this detected account type at this financial institution."""


class DetectedAccountDict(TypedDict):
    account_type: str | None
    account_subtype: str | None
    transaction_count: int
    oldest_transaction_date: NotRequired[Date]
    newest_transaction_date: NotRequired[Date]
    newest_transaction_amount: NotRequired[float]
    total_outflows: float
    total_inflows: float
