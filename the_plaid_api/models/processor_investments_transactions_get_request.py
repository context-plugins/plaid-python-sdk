from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .investments_transactions_get_request_options import (
    InvestmentsTransactionsGetRequestOptions,
    InvestmentsTransactionsGetRequestOptionsDict,
)


class ProcessorInvestmentsTransactionsGetRequest(SdkBaseModel):
    """ProcessorInvestmentsTransactionsGetRequest defines the request schema for
    ``/processor/investments/transactions/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    options: Optional[InvestmentsTransactionsGetRequestOptions] = UNSET
    """An optional object to filter ``/investments/transactions/get`` results. If provided, must be non-``null``."""

    processor_token: str
    """The processor token obtained from the Plaid integration partner. Processor tokens are in the format:
    ``processor-<environment>-<identifier>``"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: Date
    """The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD."""

    end_date: Date
    """The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD."""


class ProcessorInvestmentsTransactionsGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    options: NotRequired[InvestmentsTransactionsGetRequestOptionsDict]
    processor_token: str
    secret: NotRequired[str]
    start_date: Date
    end_date: Date
