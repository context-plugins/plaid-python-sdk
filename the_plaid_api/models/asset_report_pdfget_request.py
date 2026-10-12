from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .asset_report_pdfget_request_options import AssetReportPdfgetRequestOptions, AssetReportPdfgetRequestOptionsDict


class AssetReportPdfgetRequest(SdkBaseModel):
    """AssetReportPDFGetRequest defines the request schema for ``/asset_report/pdf/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    asset_report_token: str
    """A token that can be provided to endpoints such as ``/asset_report/get`` or ``/asset_report/pdf/get`` to fetch or
    update an Asset Report."""

    options: Optional[AssetReportPdfgetRequestOptions] = UNSET
    """An optional object to filter or add data to ``/asset_report/get`` results. If provided, must be non-``null``."""


class AssetReportPdfgetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    asset_report_token: str
    options: NotRequired[AssetReportPdfgetRequestOptionsDict]
