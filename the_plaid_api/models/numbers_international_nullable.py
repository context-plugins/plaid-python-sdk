from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersInternationalNullable(SdkBaseModel):
    """Identifying information for transferring money to or from an international bank account via wire transfer."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    iban: str
    """The International Bank Account Number (IBAN) for the account"""

    bic: str
    """The Business Identifier Code (BIC) for the account"""


class NumbersInternationalNullableDict(TypedDict):
    account_id: str
    iban: str
    bic: str
