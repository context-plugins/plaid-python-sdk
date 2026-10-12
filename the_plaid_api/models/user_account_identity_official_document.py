from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .user_account_identity_edit_counts import UserAccountIdentityEditCounts, UserAccountIdentityEditCountsDict


class UserAccountIdentityOfficialDocument(SdkBaseModel):
    """Official identity document edit statistics."""

    ssn: Optional[UserAccountIdentityEditCounts] = UNSET
    """Edit counts over various time periods."""


class UserAccountIdentityOfficialDocumentDict(TypedDict):
    ssn: NotRequired[UserAccountIdentityEditCountsDict]
