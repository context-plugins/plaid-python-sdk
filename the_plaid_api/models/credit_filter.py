from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.credit_account_subtype import CreditAccountSubtypeOrStr


class CreditFilter(SdkBaseModel):
    """A filter to apply to ``credit``-type accounts"""

    account_subtypes: list[CreditAccountSubtypeOrStr]
    """An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full
    list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""


class CreditFilterDict(TypedDict):
    account_subtypes: list[CreditAccountSubtypeOrStr]
