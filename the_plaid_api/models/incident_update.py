from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status1 import Status1OrStr


class IncidentUpdate(SdkBaseModel):
    """An update on the health incident"""

    description: Optional[str] = UNSET
    """The content of the update."""

    status: Optional[Status1OrStr] = UNSET
    """The status of the incident."""

    updated_date: Optional[RFC3339DateTime] = UNSET
    """The date when the update was published, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2020-10-30T15:26:48Z"``."""


class IncidentUpdateDict(TypedDict):
    description: NotRequired[str]
    status: NotRequired[Status1OrStr]
    updated_date: NotRequired[RFC3339DateTime]
