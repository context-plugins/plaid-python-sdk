from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class StatementsRefreshRequest(SdkBaseModel):
    """StatementsRefreshRequest defines the request schema for ``/statements/refresh``"""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: Date
    """The start date for statements, in "YYYY-MM-DD" format, e.g. "2023-08-30". To determine whether a statement falls
    within the specified date range, Plaid will use the statement posted date. The statement posted date is typically
    either the last day of the statement period, or the following day."""

    end_date: Date
    """The end date for statements, in "YYYY-MM-DD" format, e.g. "2023-10-30". You can request up to two years of data.
    To determine whether a statement falls within the specified date range, Plaid will use the statement posted date.
    The statement posted date is typically either the last day of the statement period, or the following day."""


class StatementsRefreshRequestDict(TypedDict):
    access_token: str
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_date: Date
    end_date: Date
