from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.transfer_diligence_status import TransferDiligenceStatusOrStr


class Originator(SdkBaseModel):
    """Originator and their status."""

    client_id: str
    """Originator's client ID."""

    transfer_diligence_status: TransferDiligenceStatusOrStr
    """Originator's diligence status."""


class OriginatorDict(TypedDict):
    client_id: str
    transfer_diligence_status: TransferDiligenceStatusOrStr
