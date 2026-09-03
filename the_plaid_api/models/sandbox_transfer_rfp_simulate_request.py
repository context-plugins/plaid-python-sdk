from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sandbox_transfer_rfp_simulate_action import SandboxTransferRfpSimulateActionOrStr


class SandboxTransferRfpSimulateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/rfp/simulate``"""

    transfer_id: str
    """Plaid's unique identifier for a transfer."""

    action: SandboxTransferRfpSimulateActionOrStr
    """The action to simulate. Must be either ``approve`` or ``reject``.

    - ``approve``: Simulates bank approval, transitioning the transfer to ``settled`` status
    - ``reject``: Simulates bank rejection, transitioning the transfer to ``failed`` status"""

    amount: str
    """The transfer amount provided by the caller for validation purposes, must match the amount on the transfer
    associated with the provided ``transfer_id``."""

    client_name: str
    """The client name provided by the caller for validation purposes, must match the sender client name on the transfer
    associated with the provided ``transfer_id``."""


class SandboxTransferRfpSimulateRequestDict(TypedDict):
    transfer_id: str
    action: SandboxTransferRfpSimulateActionOrStr
    amount: str
    client_name: str
