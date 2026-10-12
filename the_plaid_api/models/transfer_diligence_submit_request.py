from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_originator_diligence import TransferOriginatorDiligence, TransferOriginatorDiligenceDict


class TransferDiligenceSubmitRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/diligence/submit``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    originator_client_id: str
    """Client ID of the originator whose diligence that you want to submit."""

    originator_diligence: TransferOriginatorDiligence
    """The diligence information for the originator."""


class TransferDiligenceSubmitRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    originator_client_id: str
    originator_diligence: TransferOriginatorDiligenceDict
