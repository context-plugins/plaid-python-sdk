from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .institution import Institution, InstitutionDict


class InstitutionsGetResponse(SdkBaseModel):
    """InstitutionsGetResponse defines the response schema for ``/institutions/get``"""

    institutions: list[Institution]
    """A list of Plaid institutions"""

    total: int
    """The total number of institutions available via this endpoint"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class InstitutionsGetResponseDict(TypedDict):
    institutions: list[InstitutionDict]
    total: int
    request_id: str
