from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.account_subtype import AccountSubtypeOrStr


class InstitutionsSearchAccountFilter(SdkBaseModel):
    """An account filter to apply to institutions search requests"""

    loan: OptionalNullable[list[AccountSubtypeOrStr]] = UNSET
    depository: OptionalNullable[list[AccountSubtypeOrStr]] = UNSET
    credit: OptionalNullable[list[AccountSubtypeOrStr]] = UNSET
    investment: OptionalNullable[list[AccountSubtypeOrStr]] = UNSET


class InstitutionsSearchAccountFilterDict(TypedDict):
    loan: NotRequired[list[AccountSubtypeOrStr] | None]
    depository: NotRequired[list[AccountSubtypeOrStr] | None]
    credit: NotRequired[list[AccountSubtypeOrStr] | None]
    investment: NotRequired[list[AccountSubtypeOrStr] | None]
