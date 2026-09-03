from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.action_state import ActionStateOrStr
from .enums.activity_type import ActivityTypeOrStr
from .enums.item_create_authentication import ItemCreateAuthenticationOrStr
from .scopes_nullable import ScopesNullable, ScopesNullableDict


class Activity(SdkBaseModel):
    """Describes a consent activity."""

    activity: ActivityTypeOrStr
    """Types of consent activities"""

    initiated_date: Date
    """The date this activity was initiated `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format in
    UTC."""

    id: str
    """A unique identifier for the activity"""

    initiator: str
    """Application ID of the client who initiated the activity."""

    state: ActionStateOrStr
    """Enum representing the state of the action/activity."""

    target_application_id: Optional[str] = UNSET
    """This field will map to the application ID that is returned from ``/item/application/list``, or provided to the
    institution in an oauth redirect."""

    scopes: OptionalNullable[ScopesNullable] = UNSET
    """The scopes object"""

    authentication: Optional[ItemCreateAuthenticationOrStr] = UNSET
    """Enum representing the entity authenticating the user."""


class ActivityDict(TypedDict):
    activity: ActivityTypeOrStr
    initiated_date: Date
    id: str
    initiator: str
    state: ActionStateOrStr
    target_application_id: NotRequired[str]
    scopes: NotRequired[ScopesNullable | ScopesNullableDict | None]
    authentication: NotRequired[ItemCreateAuthenticationOrStr]
