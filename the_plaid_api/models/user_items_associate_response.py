from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserItemsAssociateResponse(SdkBaseModel):
    """UserItemsAssociateResponse defines the response schema for ``/user/items/associate``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class UserItemsAssociateResponseDict(TypedDict):
    request_id: str
