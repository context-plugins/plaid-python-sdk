from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .recurring_transfer import RecurringTransfer, RecurringTransferDict


class TransferRecurringListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/recurring/list``"""

    recurring_transfers: list[RecurringTransfer]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferRecurringListResponseDict(TypedDict):
    recurring_transfers: list[RecurringTransferDict]
    request_id: str
