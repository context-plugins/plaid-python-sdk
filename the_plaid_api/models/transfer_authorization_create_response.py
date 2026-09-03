from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_authorization import TransferAuthorization, TransferAuthorizationDict


class TransferAuthorizationCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/authorization/create``"""

    authorization: TransferAuthorization
    """Contains the authorization decision for a proposed transfer."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferAuthorizationCreateResponseDict(TypedDict):
    authorization: TransferAuthorization | TransferAuthorizationDict
    request_id: str
