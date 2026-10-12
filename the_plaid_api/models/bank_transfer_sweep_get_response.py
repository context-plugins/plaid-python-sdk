from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_transfer_sweep import BankTransferSweep, BankTransferSweepDict


class BankTransferSweepGetResponse(SdkBaseModel):
    """BankTransferSweepGetResponse defines the response schema for ``/bank_transfer/sweep/get``"""

    sweep: BankTransferSweep
    """BankTransferSweep describes a sweep transfer."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferSweepGetResponseDict(TypedDict):
    sweep: BankTransferSweepDict
    request_id: str
