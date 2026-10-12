from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transactions_sync_request_options import TransactionsSyncRequestOptions, TransactionsSyncRequestOptionsDict


class TransactionsSyncRequest(SdkBaseModel):
    """TransactionsSyncRequest defines the request schema for ``/transactions/sync``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    cursor: Optional[str] = UNSET
    """The cursor value represents the last update requested. Providing it will cause the response to only return
    changes after this update. If omitted, the entire history of updates will be returned, starting with the first-added
    transactions on the Item. The cursor also accepts the special value of ``"now"``, which can be used to fast-forward
    the cursor as part of migrating an existing Item from ``/transactions/get`` to ``/transactions/sync``. For more
    information, see the `Transactions sync migration guide <https://plaid.com/docs/transactions/sync-migration/>`__.
    Note that using the ``"now"`` value is not supported for any use case other than migrating existing Items from
    ``/transactions/get``.

    The upper-bound length of this cursor is 256 characters of base64."""

    count: int = 100
    """The number of transaction updates to fetch."""

    options: Optional[TransactionsSyncRequestOptions] = UNSET
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""


class TransactionsSyncRequestDict(TypedDict):
    client_id: NotRequired[str]
    access_token: str
    secret: NotRequired[str]
    cursor: NotRequired[str]
    count: NotRequired[int]
    options: NotRequired[TransactionsSyncRequestOptionsDict]
