from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .activity import Activity, ActivityDict
from .last_data_access_times import LastDataAccessTimes, LastDataAccessTimesDict


class ItemActivityListResponse(SdkBaseModel):
    """Describes a historical log of user consent events."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    activities: list[Activity]
    """A list of activities."""

    last_data_access_times: list[LastDataAccessTimes]
    """An array of objects containing timestamps for the last time each data type was accessed per application."""

    cursor: Optional[str] = UNSET
    """Cursor used for pagination."""


class ItemActivityListResponseDict(TypedDict):
    request_id: str
    activities: list[ActivityDict]
    last_data_access_times: list[LastDataAccessTimesDict]
    cursor: NotRequired[str]
