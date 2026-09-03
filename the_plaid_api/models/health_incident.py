from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .incident_update import IncidentUpdate, IncidentUpdateDict


class HealthIncident(SdkBaseModel):
    """A status health incident"""

    start_date: RFC3339DateTime
    """The start date of the incident, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2020-10-30T15:26:48Z"``."""

    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The end date of the incident, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2020-10-30T15:26:48Z"``."""

    title: str
    """The title of the incident"""

    incident_updates: list[IncidentUpdate]
    """Updates on the health incident."""


class HealthIncidentDict(TypedDict):
    start_date: RFC3339DateTime
    end_date: NotRequired[RFC3339DateTime | None]
    title: str
    incident_updates: list[IncidentUpdate | IncidentUpdateDict]
