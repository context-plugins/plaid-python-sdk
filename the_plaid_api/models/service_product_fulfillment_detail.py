from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.service_product_fulfillment_identifier import ServiceProductFulfillmentIdentifierOrStr


class ServiceProductFulfillmentDetail(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    vendor_order_identifier: str | None = Field(alias="VendorOrderIdentifier")
    """A string that uniquely identifies a type of order Verification of Asset."""

    service_product_fulfillment_identifier: ServiceProductFulfillmentIdentifierOrStr = Field(
        alias="ServiceProductFulfillmentIdentifier"
    )
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class ServiceProductFulfillmentDetailDict(TypedDict):
    vendor_order_identifier: str | None
    service_product_fulfillment_identifier: ServiceProductFulfillmentIdentifierOrStr
