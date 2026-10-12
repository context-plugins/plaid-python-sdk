from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .individual import Individual, IndividualDict
from .roles import Roles, RolesDict
from .taxpayer_identifiers import TaxpayerIdentifiers, TaxpayerIdentifiersDict


class Party(SdkBaseModel):
    """A collection of information about a single party to a transaction. Includes direct participants like the borrower
    and seller as well as indirect participants such as the flood certificate provider."""

    individual: Individual = Field(alias="INDIVIDUAL")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    roles: Roles = Field(alias="ROLES")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    taxpayer_identifiers: TaxpayerIdentifiers = Field(alias="TAXPAYER_IDENTIFIERS")
    """The collection of ``TAXPAYER_IDENTIFICATION`` elements"""


class PartyDict(TypedDict):
    individual: IndividualDict
    roles: RolesDict
    taxpayer_identifiers: TaxpayerIdentifiersDict
