from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.country_code import CountryCodeOrStr
from .institutions_get_request_options import InstitutionsGetRequestOptions, InstitutionsGetRequestOptionsDict


class InstitutionsGetRequest(SdkBaseModel):
    """InstitutionsGetRequest defines the request schema for ``/institutions/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    count: int
    """The total number of Institutions to return."""

    offset: int
    """The number of Institutions to skip."""

    country_codes: list[CountryCodeOrStr]
    """Specify which country or countries to include institutions from, using the ISO-3166-1 alpha-2 country code
    standard.

    In API versions 2019-05-29 and earlier, the ``country_codes`` parameter is an optional parameter within the
    ``options`` object and will default to ``[US]`` if it is not supplied."""

    options: Optional[InstitutionsGetRequestOptions] = UNSET
    """An optional object to filter ``/institutions/get`` results."""


class InstitutionsGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    count: int
    offset: int
    country_codes: list[CountryCodeOrStr]
    options: NotRequired[InstitutionsGetRequestOptions | InstitutionsGetRequestOptionsDict]
