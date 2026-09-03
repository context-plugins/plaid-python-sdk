from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transactions_sync_request_options import TransactionsSyncRequestOptions, TransactionsSyncRequestOptionsDict


class ProcessorTransactionsSyncRequest(SdkBaseModel):
    """ProcessorTransactionsSyncRequest defines the request schema for ``/processor/transactions/sync``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    processor_token: str
    """The processor token obtained from the Plaid integration partner. Processor tokens are in the format:
    ``processor-<environment>-<identifier>``"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    cursor: Optional[str] = UNSET
    """The cursor value represents the last update requested. Providing it will cause the response to only return
    changes after this update. If omitted, the entire history of updates will be returned, starting with the first-added
    transactions on the Item. Note: The upper-bound length of this cursor is 256 characters of base64."""

    count: Optional[int] = UNSET
    """The number of transaction updates to fetch."""

    options: Optional[TransactionsSyncRequestOptions] = UNSET
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""


class ProcessorTransactionsSyncRequestDict(TypedDict):
    client_id: NotRequired[str]
    processor_token: str
    secret: NotRequired[str]
    cursor: NotRequired[str]
    count: NotRequired[int]
    options: NotRequired[TransactionsSyncRequestOptions | TransactionsSyncRequestOptionsDict]
