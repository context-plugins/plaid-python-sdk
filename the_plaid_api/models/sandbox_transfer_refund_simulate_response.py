from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxTransferRefundSimulateResponse(SdkBaseModel):
    """Defines the response schema for ``/sandbox/transfer/refund/simulate``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxTransferRefundSimulateResponseDict(TypedDict):
    request_id: str
