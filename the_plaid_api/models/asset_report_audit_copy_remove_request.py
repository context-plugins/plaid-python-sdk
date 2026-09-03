from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AssetReportAuditCopyRemoveRequest(SdkBaseModel):
    """AssetReportAuditCopyRemoveRequest defines the request schema for ``/asset_report/audit_copy/remove``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    audit_copy_token: str
    """The ``audit_copy_token`` granting access to the Audit Copy you would like to revoke."""


class AssetReportAuditCopyRemoveRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    audit_copy_token: str
