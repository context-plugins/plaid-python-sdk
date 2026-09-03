from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.products import ProductsOrStr


class ProcessorTokenPermissionsGetResponse(SdkBaseModel):
    """ProcessorTokenPermissionsGetResponse defines the response schema for ``/processor/token/permissions/get``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    products: list[ProductsOrStr]
    """A list of products the processor token should have access to. An empty list means that the processor has access
    to all available products, including future products."""


class ProcessorTokenPermissionsGetResponseDict(TypedDict):
    request_id: str
    products: list[ProductsOrStr]
