from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NumbersRetirement401K(SdkBaseModel):
    """Identifying information for transferring holdings from a 401k account to another 401k account or IRA via the
    manual 401k rollover process."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    plan: Optional[str] = UNSET
    """The plan number for the employer's 401k retirement plan"""

    account: Optional[str] = UNSET
    """The full account number for the account"""


class NumbersRetirement401KDict(TypedDict):
    account_id: str
    plan: NotRequired[str]
    account: NotRequired[str]
