from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Name(SdkBaseModel):
    """Parent container for name that allows for choice group between parsed and unparsed containers."""

    first_name: str = Field(alias="FirstName")
    """The first name of the individual represented by the parent object."""

    last_name: str = Field(alias="LastName")
    """The last name of the individual represented by the parent object."""


class NameDict(TypedDict):
    first_name: str
    last_name: str
