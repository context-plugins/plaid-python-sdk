from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .asset_report_get_request_options import AssetReportGetRequestOptions, AssetReportGetRequestOptionsDict


class AssetReportGetRequest(SdkBaseModel):
    """AssetReportGetRequest defines the request schema for ``/asset_report/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    asset_report_token: Optional[str] = UNSET
    """A token that can be provided to endpoints such as ``/asset_report/get`` or ``/asset_report/pdf/get`` to fetch or
    update an Asset Report."""

    user_token: Optional[str] = UNSET
    """The user token associated with the User for which to create an asset report for. The latest asset report
    associated with the User will be returned"""

    include_insights: bool = False
    """``true`` if you would like to retrieve the Asset Report with Insights, ``false`` otherwise. This field defaults
    to ``false`` if omitted."""

    fast_report: bool = False
    """``true`` to fetch "fast" version of asset report. Defaults to false if omitted. Can only be used if
    ``/asset_report/create`` was called with ``options.add_ons`` set to ``["fast_assets"]``."""

    options: Optional[AssetReportGetRequestOptions] = UNSET
    """An optional object to filter or add data to ``/asset_report/get`` results. If provided, must be non-``null``."""


class AssetReportGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    asset_report_token: NotRequired[str]
    user_token: NotRequired[str]
    include_insights: NotRequired[bool]
    fast_report: NotRequired[bool]
    options: NotRequired[AssetReportGetRequestOptionsDict]
