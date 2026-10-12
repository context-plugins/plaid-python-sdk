from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .user_account_identity import UserAccountIdentity, UserAccountIdentityDict
from .user_account_identity_edit_history import UserAccountIdentityEditHistory, UserAccountIdentityEditHistoryDict
from .user_account_item import UserAccountItem, UserAccountItemDict


class UserAccountSessionGetResponse(SdkBaseModel):
    """UserAccountSessionGetResponse defines the response schema for ``/user_account/session/get``"""

    identity: UserAccountIdentity | None
    """The identity data permissioned by the end user during the authorization flow."""

    items: list[UserAccountItem]
    identity_edit_history: OptionalNullable[UserAccountIdentityEditHistory] = UNSET
    """Statistics tracking the number of edits made to identity fields over various time periods."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class UserAccountSessionGetResponseDict(TypedDict):
    identity: UserAccountIdentityDict | None
    items: list[UserAccountItemDict]
    identity_edit_history: NotRequired[UserAccountIdentityEditHistoryDict | None]
    request_id: str
