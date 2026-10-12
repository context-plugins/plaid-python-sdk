from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_filters_response import AccountFiltersResponse, AccountFiltersResponseDict
from .enums.country_code import CountryCodeOrStr
from .enums.products import ProductsOrStr
from .link_token_create_institution_data import LinkTokenCreateInstitutionData, LinkTokenCreateInstitutionDataDict


class LinkTokenGetMetadataResponse(SdkBaseModel):
    """An object specifying the arguments originally provided to the ``/link/token/create`` call."""

    initial_products: list[ProductsOrStr]
    """The ``products`` specified in the ``/link/token/create`` call."""

    webhook: str | None
    """The ``webhook`` specified in the ``/link/token/create`` call."""

    country_codes: list[CountryCodeOrStr]
    """The ``country_codes`` specified in the ``/link/token/create`` call."""

    language: str | None
    """The ``language`` specified in the ``/link/token/create`` call."""

    institution_data: Optional[LinkTokenCreateInstitutionData] = UNSET
    """A map containing data used to highlight institutions in Link."""

    account_filters: Optional[AccountFiltersResponse] = UNSET
    """The ``account_filters`` specified in the original call to ``/link/token/create``."""

    redirect_uri: str | None
    """The ``redirect_uri`` specified in the ``/link/token/create`` call."""

    client_name: str | None
    """The ``client_name`` specified in the ``/link/token/create`` call."""


class LinkTokenGetMetadataResponseDict(TypedDict):
    initial_products: list[ProductsOrStr]
    webhook: str | None
    country_codes: list[CountryCodeOrStr]
    language: str | None
    institution_data: NotRequired[LinkTokenCreateInstitutionDataDict]
    account_filters: NotRequired[AccountFiltersResponseDict]
    redirect_uri: str | None
    client_name: str | None
