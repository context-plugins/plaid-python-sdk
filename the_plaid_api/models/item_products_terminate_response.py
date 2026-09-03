from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ItemProductsTerminateResponse(SdkBaseModel):
    """ItemProductsTerminateResponse defines the response schema for ``/item/products/terminate``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemProductsTerminateResponseDict(TypedDict):
    request_id: str
