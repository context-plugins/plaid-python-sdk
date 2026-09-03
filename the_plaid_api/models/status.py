from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Status(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    status_code: str | None = Field(alias="StatusCode")
    """Status Code."""

    status_description: str | None = Field(alias="StatusDescription")
    """Status Description."""


class StatusDict(TypedDict):
    status_code: str | None
    status_description: str | None
