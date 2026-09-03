from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cashflow_report_get_request_options import CashflowReportGetRequestOptions, CashflowReportGetRequestOptionsDict


class CashflowReportGetRequest(SdkBaseModel):
    """CashflowReportGetRequest defines the request schema for ``/cashflow_report/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    days_requested: int
    """Number of days to retrieve transactions data for (1 to 730)"""

    count: Optional[int] = UNSET
    """Number of transactions to fetch per call"""

    cursor: Optional[str] = UNSET
    """The cursor value represents the last update requested. Pass in the empty string "" in the first call."""

    options: Optional[CashflowReportGetRequestOptions] = UNSET
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""


class CashflowReportGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    access_token: str
    secret: NotRequired[str]
    days_requested: int
    count: NotRequired[int]
    cursor: NotRequired[str]
    options: NotRequired[CashflowReportGetRequestOptions | CashflowReportGetRequestOptionsDict]
