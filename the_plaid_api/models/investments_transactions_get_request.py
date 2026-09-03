from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .investments_transactions_get_request_options import (
    InvestmentsTransactionsGetRequestOptions,
    InvestmentsTransactionsGetRequestOptionsDict,
)


class InvestmentsTransactionsGetRequest(SdkBaseModel):
    """InvestmentsTransactionsGetRequest defines the request schema for ``/investments/transactions/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    start_date: Date
    """The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD."""

    end_date: Date
    """The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD."""

    options: Optional[InvestmentsTransactionsGetRequestOptions] = UNSET
    """An optional object to filter ``/investments/transactions/get`` results. If provided, must be non-``null``."""


class InvestmentsTransactionsGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    start_date: Date
    end_date: Date
    options: NotRequired[InvestmentsTransactionsGetRequestOptions | InvestmentsTransactionsGetRequestOptionsDict]
