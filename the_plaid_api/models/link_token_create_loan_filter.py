from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.loan_account_subtype import LoanAccountSubtypeOrStr


class LinkTokenCreateLoanFilter(SdkBaseModel):
    """A filter to apply to ``loan``-type accounts"""

    account_subtypes: Optional[list[LoanAccountSubtypeOrStr]] = UNSET
    """An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full
    list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""


class LinkTokenCreateLoanFilterDict(TypedDict):
    account_subtypes: NotRequired[list[LoanAccountSubtypeOrStr]]
