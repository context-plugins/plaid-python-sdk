from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BankTransferCancelResponse(SdkBaseModel):
    """Defines the response schema for ``/bank_transfer/cancel``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferCancelResponseDict(TypedDict):
    request_id: str
