from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .role import Role, RoleDict


class Roles(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    role: Role = Field(alias="ROLE")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class RolesDict(TypedDict):
    role: RoleDict
