from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditFreddieMacIndividualName(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    first_name: str = Field(alias="FirstName")
    """The first name of the individual represented by the parent object."""

    last_name: str = Field(alias="LastName")
    """The last name of the individual represented by the parent object."""

    middle_name: str = Field(alias="MiddleName")
    """The middle name of the individual represented by the parent object."""


class CreditFreddieMacIndividualNameDict(TypedDict):
    first_name: str
    last_name: str
    middle_name: str
