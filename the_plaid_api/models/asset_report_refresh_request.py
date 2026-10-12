from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .asset_report_refresh_request_options import AssetReportRefreshRequestOptions, AssetReportRefreshRequestOptionsDict


class AssetReportRefreshRequest(SdkBaseModel):
    """AssetReportRefreshRequest defines the request schema for ``/asset_report/refresh``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    asset_report_token: str
    """The ``asset_report_token`` returned by the original call to ``/asset_report/create``"""

    days_requested: OptionalNullable[int] = UNSET
    """The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the
    value from the original call to ``/asset_report/create`` will be used."""

    options: Optional[AssetReportRefreshRequestOptions] = UNSET
    """An optional object to filter ``/asset_report/refresh`` results. If provided, cannot be ``null``. If not
    specified, the ``options`` from the original call to ``/asset_report/create`` will be used."""


class AssetReportRefreshRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    asset_report_token: str
    days_requested: NotRequired[int | None]
    options: NotRequired[AssetReportRefreshRequestOptionsDict]
