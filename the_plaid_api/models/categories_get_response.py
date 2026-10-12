from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category import Category, CategoryDict


class CategoriesGetResponse(SdkBaseModel):
    """CategoriesGetResponse defines the response schema for ``/categories/get``"""

    categories: list[Category]
    """An array of all of the transaction categories used by Plaid."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CategoriesGetResponseDict(TypedDict):
    categories: list[CategoryDict]
    request_id: str
