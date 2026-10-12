from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_transfer_sweep import BankTransferSweep, BankTransferSweepDict


class BankTransferSweepListResponse(SdkBaseModel):
    """BankTransferSweepListResponse defines the response schema for ``/bank_transfer/sweep/list``"""

    sweeps: list[BankTransferSweep]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferSweepListResponseDict(TypedDict):
    sweeps: list[BankTransferSweepDict]
    request_id: str
