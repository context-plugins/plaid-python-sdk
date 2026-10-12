from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_report import AssetReport, AssetReportDict
from .warning_model import WarningModel, WarningModelDict


class AssetReportGetResponse(SdkBaseModel):
    """AssetReportGetResponse defines the response schema for ``/asset_report/get``"""

    report: AssetReport
    """An object representing an Asset Report"""

    warnings: list[WarningModel]
    """If the Asset Report generation was successful but identity information cannot be returned, this array will
    contain information about the errors causing identity information to be missing"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class AssetReportGetResponseDict(TypedDict):
    report: AssetReportDict
    warnings: list[WarningModelDict]
    request_id: str
