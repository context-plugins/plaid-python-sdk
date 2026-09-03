from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersBacs(SdkBaseModel):
    """Identifying information for transferring money to or from a UK bank account via Bacs."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    account: str
    """The Bacs account number for the account"""

    sort_code: str
    """The Bacs sort code for the account"""


class NumbersBacsDict(TypedDict):
    account_id: str
    account: str
    sort_code: str
