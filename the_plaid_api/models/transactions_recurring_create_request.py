from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transactions_recurring_create_input import TransactionsRecurringCreateInput, TransactionsRecurringCreateInputDict


class TransactionsRecurringCreateRequest(SdkBaseModel):
    """TransactionsRecurringCreateRequest defines the request schema for ``/transactions/recurring/streams/create``
    endpoint."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    inputs: list[TransactionsRecurringCreateInput]
    """A list of all the operations to be performed. This will either all succeed or all fail."""


class TransactionsRecurringCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    access_token: str
    secret: NotRequired[str]
    inputs: list[TransactionsRecurringCreateInput | TransactionsRecurringCreateInputDict]
