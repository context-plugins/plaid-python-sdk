from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferOriginatorCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/originator/create``"""

    originator_client_id: str
    """Client ID of the originator. This identifier will be used when creating transfers and should be stored associated
    with end user information."""

    company_name: str
    """The company name of the end customer."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferOriginatorCreateResponseDict(TypedDict):
    originator_client_id: str
    company_name: str
    request_id: str
