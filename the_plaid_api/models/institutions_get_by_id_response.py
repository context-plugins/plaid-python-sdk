from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .institution import Institution, InstitutionDict


class InstitutionsGetByIdResponse(SdkBaseModel):
    """InstitutionsGetByIdResponse defines the response schema for ``/institutions/get_by_id``"""

    institution: Institution
    """Details relating to a specific financial institution"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class InstitutionsGetByIdResponseDict(TypedDict):
    institution: InstitutionDict
    request_id: str
