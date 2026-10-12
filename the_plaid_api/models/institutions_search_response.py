from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .institution import Institution, InstitutionDict


class InstitutionsSearchResponse(SdkBaseModel):
    """InstitutionsSearchResponse defines the response schema for ``/institutions/search``"""

    institutions: list[Institution]
    """An array of institutions matching the search criteria"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class InstitutionsSearchResponseDict(TypedDict):
    institutions: list[InstitutionDict]
    request_id: str
