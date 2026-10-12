from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_subtype import AccountSubtypeOrStr


class InstitutionsSearchAccountFilter(SdkBaseModel):
    """An account filter to apply to institutions search requests"""

    loan: Optional[list[AccountSubtypeOrStr | None]] = UNSET
    depository: Optional[list[AccountSubtypeOrStr | None]] = UNSET
    credit: Optional[list[AccountSubtypeOrStr | None]] = UNSET
    investment: Optional[list[AccountSubtypeOrStr | None]] = UNSET


class InstitutionsSearchAccountFilterDict(TypedDict):
    loan: NotRequired[list[AccountSubtypeOrStr | None]]
    depository: NotRequired[list[AccountSubtypeOrStr | None]]
    credit: NotRequired[list[AccountSubtypeOrStr | None]]
    investment: NotRequired[list[AccountSubtypeOrStr | None]]
