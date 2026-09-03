from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersAton(SdkBaseModel):
    """Identifying information for transferring holdings to an investment account via ATON."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    account: str
    """The full account number for the account"""


class NumbersAtonDict(TypedDict):
    account_id: str
    account: str
