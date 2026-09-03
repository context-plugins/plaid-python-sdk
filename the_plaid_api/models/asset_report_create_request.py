from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .asset_report_create_request_options import AssetReportCreateRequestOptions, AssetReportCreateRequestOptionsDict


class AssetReportCreateRequest(SdkBaseModel):
    """AssetReportCreateRequest defines the request schema for ``/asset_report/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_tokens: Optional[list[str]] = UNSET
    """An array of access tokens corresponding to the Items that will be included in the report. The ``assets`` product
    must have been initialized for the Items during Link; the Assets product cannot be added after initialization."""

    days_requested: int
    """The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1
    Certainty, ``days_requested`` must be at least 61 for new originations or at least 31 for refinancings.

    An Asset Report requested with "Additional History" (that is, with more than 61 days of transaction history) will
    incur an Additional History fee."""

    options: Optional[AssetReportCreateRequestOptions] = UNSET
    """An optional object to filter ``/asset_report/create`` results. If provided, must be non-``null``. The optional
    ``user`` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program."""


class AssetReportCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_tokens: NotRequired[list[str]]
    days_requested: int
    options: NotRequired[AssetReportCreateRequestOptions | AssetReportCreateRequestOptionsDict]
