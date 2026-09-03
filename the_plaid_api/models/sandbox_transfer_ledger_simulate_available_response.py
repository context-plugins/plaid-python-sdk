from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxTransferLedgerSimulateAvailableResponse(SdkBaseModel):
    """Defines the response schema for ``/sandbox/transfer/ledger/simulate_available``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxTransferLedgerSimulateAvailableResponseDict(TypedDict):
    request_id: str
