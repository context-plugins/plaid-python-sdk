from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxBankTransferSimulateResponse(SdkBaseModel):
    """Defines the response schema for ``/sandbox/bank_transfer/simulate``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxBankTransferSimulateResponseDict(TypedDict):
    request_id: str
