from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_individual_name import CreditFreddieMacIndividualName, CreditFreddieMacIndividualNameDict


class CreditFreddieMacPartyIndividual(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    name: CreditFreddieMacIndividualName = Field(alias="NAME")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class CreditFreddieMacPartyIndividualDict(TypedDict):
    name: CreditFreddieMacIndividualNameDict
