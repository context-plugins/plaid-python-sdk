from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .user_account_identity_edit_counts import UserAccountIdentityEditCounts, UserAccountIdentityEditCountsDict
from .user_account_identity_official_document import (
    UserAccountIdentityOfficialDocument,
    UserAccountIdentityOfficialDocumentDict,
)


class UserAccountIdentityEditHistory(SdkBaseModel):
    """Statistics tracking the number of edits made to identity fields over various time periods."""

    name: Optional[UserAccountIdentityEditCounts] = UNSET
    """Edit counts over various time periods."""

    address: Optional[UserAccountIdentityEditCounts] = UNSET
    """Edit counts over various time periods."""

    email: Optional[UserAccountIdentityEditCounts] = UNSET
    """Edit counts over various time periods."""

    date_of_birth: Optional[UserAccountIdentityEditCounts] = UNSET
    """Edit counts over various time periods."""

    official_document: OptionalNullable[UserAccountIdentityOfficialDocument] = UNSET
    """Official identity document edit statistics."""


class UserAccountIdentityEditHistoryDict(TypedDict):
    name: NotRequired[UserAccountIdentityEditCountsDict]
    address: NotRequired[UserAccountIdentityEditCountsDict]
    email: NotRequired[UserAccountIdentityEditCountsDict]
    date_of_birth: NotRequired[UserAccountIdentityEditCountsDict]
    official_document: NotRequired[UserAccountIdentityOfficialDocumentDict | None]
