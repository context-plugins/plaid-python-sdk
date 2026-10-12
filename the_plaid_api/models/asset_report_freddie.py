from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loans import Loans, LoansDict
from .parties import Parties, PartiesDict
from .services import Services, ServicesDict


class AssetReportFreddie(SdkBaseModel):
    """An object representing an Asset Report with Freddie Mac schema."""

    loans: Loans = Field(alias="LOANS")
    """A collection of loans that are part of a single deal."""

    parties: Parties = Field(alias="PARTIES")
    """A collection of objects that define specific parties to a deal. This includes the direct participating parties,
    such as borrower and seller and the indirect parties such as the credit report provider."""

    services: Services = Field(alias="SERVICES")
    """A collection of objects that describe requests and responses for services."""


class AssetReportFreddieDict(TypedDict):
    loans: LoansDict
    parties: PartiesDict
    services: ServicesDict
