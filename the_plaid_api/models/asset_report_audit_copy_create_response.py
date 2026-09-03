from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetReportAuditCopyCreateResponse(SdkBaseModel):
    """AssetReportAuditCopyCreateResponse defines the response schema for ``/asset_report/audit_copy/create``"""

    audit_copy_token: str
    """A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This
    token should be stored securely."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class AssetReportAuditCopyCreateResponseDict(TypedDict):
    audit_copy_token: str
    request_id: str
