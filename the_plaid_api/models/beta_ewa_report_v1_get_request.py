from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BetaEwaReportV1GetRequest(SdkBaseModel):
    """BetaEwaReportV1GetRequest defines the request schema for ``/beta/ewa_report/v1/get``"""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class BetaEwaReportV1GetRequestDict(TypedDict):
    access_token: str
    client_id: NotRequired[str]
    secret: NotRequired[str]
