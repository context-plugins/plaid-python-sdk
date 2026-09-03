from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersEft(SdkBaseModel):
    """Identifying information for transferring money to or from a Canadian bank account via EFT."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    account: str
    """The EFT account number for the account"""

    institution: str
    """The EFT institution number for the account"""

    branch: str
    """The EFT branch number for the account"""


class NumbersEftDict(TypedDict):
    account_id: str
    account: str
    institution: str
    branch: str
