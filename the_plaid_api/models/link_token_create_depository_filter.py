from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.depository_account_subtype import DepositoryAccountSubtypeOrStr
from .enums.limited_purpose_type import LimitedPurposeTypeOrStr


class LinkTokenCreateDepositoryFilter(SdkBaseModel):
    """A filter to apply to ``depository``-type accounts"""

    account_subtypes: Optional[list[DepositoryAccountSubtypeOrStr]] = UNSET
    """An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full
    list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""

    limited_purpose_types: Optional[list[LimitedPurposeTypeOrStr]] = UNSET
    """An array of limited purpose types. Restricts which kinds of limited purpose checking accounts may be connected in
    Link to prevent users from connecting them for unsupported use cases. Required when 'limited purpose checking' is in
    the subtypes filter."""


class LinkTokenCreateDepositoryFilterDict(TypedDict):
    account_subtypes: NotRequired[list[DepositoryAccountSubtypeOrStr]]
    limited_purpose_types: NotRequired[list[LimitedPurposeTypeOrStr]]
