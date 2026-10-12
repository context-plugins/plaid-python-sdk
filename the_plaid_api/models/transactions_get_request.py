from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .transactions_get_request_options import TransactionsGetRequestOptions, TransactionsGetRequestOptionsDict


class TransactionsGetRequest(SdkBaseModel):
    """TransactionsGetRequest defines the request schema for ``/transactions/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    options: Optional[TransactionsGetRequestOptions] = UNSET
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: Date
    """The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD."""

    end_date: Date
    """The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD."""


class TransactionsGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    options: NotRequired[TransactionsGetRequestOptionsDict]
    access_token: str
    secret: NotRequired[str]
    start_date: Date
    end_date: Date
