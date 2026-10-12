from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_reporting_information import (
    CreditFreddieMacReportingInformation,
    CreditFreddieMacReportingInformationDict,
)
from .credit_freddie_mac_verification_of_asset_response import (
    CreditFreddieMacVerificationOfAssetResponse,
    CreditFreddieMacVerificationOfAssetResponseDict,
)
from .service_product_fulfillment import ServiceProductFulfillment, ServiceProductFulfillmentDict


class CreditFreddieMacVerificationOfAsset(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    reporting_information: CreditFreddieMacReportingInformation = Field(alias="REPORTING_INFORMATION")
    """Information about a report identifier and a report name."""

    service_product_fulfillment: ServiceProductFulfillment = Field(alias="SERVICE_PRODUCT_FULFILLMENT")
    """A collection of details related to a fulfillment service or product in terms of request, process and result."""

    verification_of_asset_response: CreditFreddieMacVerificationOfAssetResponse = Field(
        alias="VERIFICATION_OF_ASSET_RESPONSE"
    )
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class CreditFreddieMacVerificationOfAssetDict(TypedDict):
    reporting_information: CreditFreddieMacReportingInformationDict
    service_product_fulfillment: ServiceProductFulfillmentDict
    verification_of_asset_response: CreditFreddieMacVerificationOfAssetResponseDict
