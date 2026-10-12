from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .role_detail import RoleDetail, RoleDetailDict


class Role(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    role_detail: RoleDetail = Field(alias="ROLE_DETAIL")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class RoleDict(TypedDict):
    role_detail: RoleDetailDict
