from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .simulated_transfer_sweep import SimulatedTransferSweep, SimulatedTransferSweepDict


class SandboxTransferSweepSimulateResponse(SdkBaseModel):
    """Defines the response schema for ``/sandbox/transfer/sweep/simulate``"""

    sweep: OptionalNullable[SimulatedTransferSweep] = UNSET
    """A sweep returned from the ``/sandbox/transfer/sweep/simulate`` endpoint. Can be null if there are no transfers to
    include in a sweep."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxTransferSweepSimulateResponseDict(TypedDict):
    sweep: NotRequired[SimulatedTransferSweepDict | None]
    request_id: str
