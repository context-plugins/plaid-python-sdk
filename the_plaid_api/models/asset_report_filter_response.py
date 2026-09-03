from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetReportFilterResponse(SdkBaseModel):
    """AssetReportFilterResponse defines the response schema for ``/asset_report/filter``"""

    asset_report_token: str
    """A token that can be provided to endpoints such as ``/asset_report/get`` or ``/asset_report/pdf/get`` to fetch or
    update an Asset Report."""

    asset_report_id: str
    """A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class AssetReportFilterResponseDict(TypedDict):
    asset_report_token: str
    asset_report_id: str
    request_id: str
