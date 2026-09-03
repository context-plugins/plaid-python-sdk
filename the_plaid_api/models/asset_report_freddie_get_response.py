from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_report_freddie import AssetReportFreddie, AssetReportFreddieDict


class AssetReportFreddieGetResponse(SdkBaseModel):
    """AssetReportFreddieGetResponse defines the response schema for ``/credit/asset_report/freddie_mac/get``"""

    deal: AssetReportFreddie = Field(alias="DEAL")
    """An object representing an Asset Report with Freddie Mac schema."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    schema_version: float = Field(alias="SchemaVersion")
    """The Verification Of Assets (aka VOA or Freddie Mac Schema) schema version."""


class AssetReportFreddieGetResponseDict(TypedDict):
    deal: AssetReportFreddie | AssetReportFreddieDict
    request_id: str
    schema_version: float
