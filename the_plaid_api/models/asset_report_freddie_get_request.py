from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AssetReportFreddieGetRequest(SdkBaseModel):
    """AssetReportFreddieGetRequest defines the request schema for ``/credit/asset_report/freddie_mac/get``"""

    audit_copy_token: str
    """A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This
    token should be stored securely."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class AssetReportFreddieGetRequestDict(TypedDict):
    audit_copy_token: str
    client_id: NotRequired[str]
    secret: NotRequired[str]
