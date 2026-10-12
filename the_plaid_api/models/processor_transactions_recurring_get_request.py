from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transactions_recurring_get_request_options import (
    TransactionsRecurringGetRequestOptions,
    TransactionsRecurringGetRequestOptionsDict,
)


class ProcessorTransactionsRecurringGetRequest(SdkBaseModel):
    """ProcessorTransactionsRecurringGetRequest defines the request schema for
    ``/processor/transactions/recurring/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    processor_token: str
    """The processor token obtained from the Plaid integration partner. Processor tokens are in the format:
    ``processor-<environment>-<identifier>``"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    options: Optional[TransactionsRecurringGetRequestOptions] = UNSET
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""


class ProcessorTransactionsRecurringGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    processor_token: str
    secret: NotRequired[str]
    options: NotRequired[TransactionsRecurringGetRequestOptionsDict]
