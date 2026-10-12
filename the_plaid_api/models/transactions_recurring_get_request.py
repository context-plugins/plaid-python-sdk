from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transactions_recurring_get_request_options import (
    TransactionsRecurringGetRequestOptions,
    TransactionsRecurringGetRequestOptionsDict,
)


class TransactionsRecurringGetRequest(SdkBaseModel):
    """TransactionsRecurringGetRequest defines the request schema for ``/transactions/recurring/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    options: Optional[TransactionsRecurringGetRequestOptions] = UNSET
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""

    account_ids: Optional[list[str]] = UNSET
    """An optional list of ``account_ids`` to retrieve for the Item. Retrieves all active accounts on item if no
    ``account_id``s are provided.

    Note: An error will be returned if a provided ``account_id`` is not associated with the Item."""


class TransactionsRecurringGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    access_token: str
    secret: NotRequired[str]
    options: NotRequired[TransactionsRecurringGetRequestOptionsDict]
    account_ids: NotRequired[list[str]]
