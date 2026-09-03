from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.products import ProductsOrStr


class CraReportGetRequestProduct(SdkBaseModel):
    """CraReportGetRequestProduct specifies a product and version for a ``/cra/report/get`` call."""

    product: ProductsOrStr
    version: str
    """The version of the product that was generated."""


class CraReportGetRequestProductDict(TypedDict):
    product: ProductsOrStr
    version: str
