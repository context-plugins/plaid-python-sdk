from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ItemApplicationScopesUpdateResponse(SdkBaseModel):
    """ItemApplicationScopesUpdateResponse defines the response schema for ``/item/application/scopes/update``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemApplicationScopesUpdateResponseDict(TypedDict):
    request_id: str
