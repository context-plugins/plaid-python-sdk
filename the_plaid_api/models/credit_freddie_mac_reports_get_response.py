from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_verification_of_assets_deal import (
    CreditFreddieMacVerificationOfAssetsDeal,
    CreditFreddieMacVerificationOfAssetsDealDict,
)


class CreditFreddieMacReportsGetResponse(SdkBaseModel):
    """CreditFreddieMacReportsGetResponse defines the response schema for ``/credit/freddie_mac/reports/get``"""

    deal: CreditFreddieMacVerificationOfAssetsDeal = Field(alias="DEAL")
    """An object representing an Asset Report with Freddie Mac schema."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    schema_version: float = Field(alias="SchemaVersion")
    """The Verification Of Assets (VOA) schema version."""


class CreditFreddieMacReportsGetResponseDict(TypedDict):
    deal: CreditFreddieMacVerificationOfAssetsDealDict
    request_id: str
    schema_version: float
