from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_sweep import TransferSweep, TransferSweepDict


class TransferSweepListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/sweep/list``"""

    sweeps: list[TransferSweep]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferSweepListResponseDict(TypedDict):
    sweeps: list[TransferSweep | TransferSweepDict]
    request_id: str
