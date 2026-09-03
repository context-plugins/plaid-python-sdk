from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_loans import CreditFreddieMacLoans, CreditFreddieMacLoansDict
from .credit_freddie_mac_parties import CreditFreddieMacParties, CreditFreddieMacPartiesDict
from .credit_freddie_mac_services import CreditFreddieMacServices, CreditFreddieMacServicesDict


class CreditFreddieMacVerificationOfAssetsDeal(SdkBaseModel):
    """An object representing an Asset Report with Freddie Mac schema."""

    loans: CreditFreddieMacLoans = Field(alias="LOANS")
    """A collection of loans that are part of a single deal."""

    parties: CreditFreddieMacParties = Field(alias="PARTIES")
    """A collection of objects that define specific parties to a deal. This includes the direct participating parties,
    such as borrower and seller and the indirect parties such as the credit report provider."""

    services: CreditFreddieMacServices = Field(alias="SERVICES")
    """A collection of objects that describe requests and responses for services."""


class CreditFreddieMacVerificationOfAssetsDealDict(TypedDict):
    loans: CreditFreddieMacLoans | CreditFreddieMacLoansDict
    parties: CreditFreddieMacParties | CreditFreddieMacPartiesDict
    services: CreditFreddieMacServices | CreditFreddieMacServicesDict
