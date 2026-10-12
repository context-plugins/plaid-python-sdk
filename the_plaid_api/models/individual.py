from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .name import Name, NameDict


class Individual(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    name: Name = Field(alias="NAME")
    """Parent container for name that allows for choice group between parsed and unparsed containers."""


class IndividualDict(TypedDict):
    name: NameDict
