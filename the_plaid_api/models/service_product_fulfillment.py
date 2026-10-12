from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .service_product_fulfillment_detail import ServiceProductFulfillmentDetail, ServiceProductFulfillmentDetailDict


class ServiceProductFulfillment(SdkBaseModel):
    """A collection of details related to a fulfillment service or product in terms of request, process and result."""

    service_product_fulfillment_detail: ServiceProductFulfillmentDetail = Field(
        alias="SERVICE_PRODUCT_FULFILLMENT_DETAIL"
    )
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class ServiceProductFulfillmentDict(TypedDict):
    service_product_fulfillment_detail: ServiceProductFulfillmentDetailDict
