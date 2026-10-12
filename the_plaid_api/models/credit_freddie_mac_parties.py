from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_party import CreditFreddieMacParty, CreditFreddieMacPartyDict


class CreditFreddieMacParties(SdkBaseModel):
    """A collection of objects that define specific parties to a deal. This includes the direct participating parties,
    such as borrower and seller and the indirect parties such as the credit report provider."""

    party: list[CreditFreddieMacParty] = Field(alias="PARTY")


class CreditFreddieMacPartiesDict(TypedDict):
    party: list[CreditFreddieMacPartyDict]
