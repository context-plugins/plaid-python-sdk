from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.report_type import ReportTypeOrStr


class CreditRelayRefreshRequest(SdkBaseModel):
    """CreditRelayRefreshRequest defines the request schema for ``/credit/relay/refresh``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    relay_token: str
    """The ``relay_token`` granting access to the report you would like to refresh."""

    report_type: ReportTypeOrStr
    """The report type. It can be ``asset``. Income report types are not yet supported."""

    webhook: OptionalNullable[str] = UNSET
    """The URL registered to receive webhooks when the report of a relay token has been refreshed."""


class CreditRelayRefreshRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    relay_token: str
    report_type: ReportTypeOrStr
    webhook: NotRequired[str | None]
