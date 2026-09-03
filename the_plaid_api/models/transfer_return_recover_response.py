from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferReturnRecoverResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/return/recover``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferReturnRecoverResponseDict(TypedDict):
    request_id: str
