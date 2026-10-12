from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.products import ProductsOrStr
from .error import Error, ErrorDict


class CraReportGetResponseProduct(SdkBaseModel):
    """Per-product report data. ``attributes`` is an opaque map of key-value pairs; for a full list of attributes per
    product and version, see the data dictionary."""

    product: ProductsOrStr
    version: str
    """The version of the product that was generated."""

    metadata: dict[str, Any] | None
    """A map of product report metadata, where the key is a string and the value varies by product. For a full list of
    metadata fields per product, see the data dictionary. May be ``null`` if metadata was not available."""

    attributes: dict[str, Any] | None
    """A map of product attributes, where the key is a string and the value can be any JSON value. The specific list of
    attributes depends on the product and version. For a full list, see the data dictionary. May be ``null`` if
    attributes were not available."""

    errors: list[Error | None]
    """Product-level errors. Non-empty when this product failed to generate; empty on success."""


class CraReportGetResponseProductDict(TypedDict):
    product: ProductsOrStr
    version: str
    metadata: dict[str, Any] | None
    attributes: dict[str, Any] | None
    errors: list[ErrorDict | None]
