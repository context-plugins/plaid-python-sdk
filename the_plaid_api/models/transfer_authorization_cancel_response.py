from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferAuthorizationCancelResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/authorization/cancel``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferAuthorizationCancelResponseDict(TypedDict):
    request_id: str
