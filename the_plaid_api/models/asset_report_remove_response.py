from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetReportRemoveResponse(SdkBaseModel):
    """AssetReportRemoveResponse defines the response schema for ``/asset_report/remove``"""

    removed: bool
    """``true`` if the Asset Report was successfully removed."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class AssetReportRemoveResponseDict(TypedDict):
    removed: bool
    request_id: str
