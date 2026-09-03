from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UserAccountIdentityName(SdkBaseModel):
    """The user's first name and last name."""

    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET


class UserAccountIdentityNameDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
