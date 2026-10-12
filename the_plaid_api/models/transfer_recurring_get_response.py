from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .recurring_transfer import RecurringTransfer, RecurringTransferDict


class TransferRecurringGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/recurring/get``"""

    recurring_transfer: RecurringTransfer
    """Represents a recurring transfer within the Transfers API."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferRecurringGetResponseDict(TypedDict):
    recurring_transfer: RecurringTransferDict
    request_id: str
