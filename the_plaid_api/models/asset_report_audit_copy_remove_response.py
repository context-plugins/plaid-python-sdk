from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetReportAuditCopyRemoveResponse(SdkBaseModel):
    """AssetReportAuditCopyRemoveResponse defines the response schema for ``/asset_report/audit_copy/remove``"""

    removed: bool
    """``true`` if the Audit Copy was successfully removed."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class AssetReportAuditCopyRemoveResponseDict(TypedDict):
    removed: bool
    request_id: str
