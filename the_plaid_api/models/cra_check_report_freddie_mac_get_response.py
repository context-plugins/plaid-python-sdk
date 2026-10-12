from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_check_report_freddie_mac_verification_of_assets_deal import (
    CraCheckReportFreddieMacVerificationOfAssetsDeal,
    CraCheckReportFreddieMacVerificationOfAssetsDealDict,
)


class CraCheckReportFreddieMacGetResponse(SdkBaseModel):
    """CraCheckReportFreddieMacGetResponse defines the response schema for ``/cra/check_report/freddie_mac/get``"""

    deal: CraCheckReportFreddieMacVerificationOfAssetsDeal = Field(alias="DEAL")
    """An object representing a Base Report with Freddie Mac schema."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    schema_version: float = Field(alias="SchemaVersion")
    """The Verification Of Assets (VOA) schema version."""


class CraCheckReportFreddieMacGetResponseDict(TypedDict):
    deal: CraCheckReportFreddieMacVerificationOfAssetsDealDict
    request_id: str
    schema_version: float
