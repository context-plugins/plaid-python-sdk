from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.loan_account_subtype import LoanAccountSubtypeOrStr


class LoanFilter(SdkBaseModel):
    """A filter to apply to ``loan``-type accounts"""

    account_subtypes: list[LoanAccountSubtypeOrStr]
    """An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full
    list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""


class LoanFilterDict(TypedDict):
    account_subtypes: list[LoanAccountSubtypeOrStr]
