from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .status import Status, StatusDict


class Statuses(SdkBaseModel):
    """A collection of STATUS containers."""

    status: Status = Field(alias="STATUS")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class StatusesDict(TypedDict):
    status: StatusDict
