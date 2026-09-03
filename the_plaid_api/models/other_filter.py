from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.other_account_subtype import OtherAccountSubtypeOrStr


class OtherFilter(SdkBaseModel):
    """A filter to apply to ``other``-type accounts"""

    account_subtypes: list[OtherAccountSubtypeOrStr]
    """An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full
    list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""


class OtherFilterDict(TypedDict):
    account_subtypes: list[OtherAccountSubtypeOrStr]
