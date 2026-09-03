from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .reporting_information import ReportingInformation, ReportingInformationDict
from .service_product_fulfillment import ServiceProductFulfillment, ServiceProductFulfillmentDict
from .verification_of_asset_response import VerificationOfAssetResponse, VerificationOfAssetResponseDict


class VerificationOfAsset(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    reporting_information: ReportingInformation = Field(alias="REPORTING_INFORMATION")
    """Information about a report identifier and a report name."""

    service_product_fulfillment: ServiceProductFulfillment = Field(alias="SERVICE_PRODUCT_FULFILLMENT")
    """A collection of details related to a fulfillment service or product in terms of request, process and result."""

    verification_of_asset_response: VerificationOfAssetResponse = Field(alias="VERIFICATION_OF_ASSET_RESPONSE")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class VerificationOfAssetDict(TypedDict):
    reporting_information: ReportingInformation | ReportingInformationDict
    service_product_fulfillment: ServiceProductFulfillment | ServiceProductFulfillmentDict
    verification_of_asset_response: VerificationOfAssetResponse | VerificationOfAssetResponseDict
