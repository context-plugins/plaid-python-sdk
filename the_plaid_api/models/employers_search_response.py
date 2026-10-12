from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .employer import Employer, EmployerDict


class EmployersSearchResponse(SdkBaseModel):
    """EmployersSearchResponse defines the response schema for ``/employers/search``."""

    employers: list[Employer]
    """A list of employers matching the search criteria."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class EmployersSearchResponseDict(TypedDict):
    employers: list[EmployerDict]
    request_id: str
