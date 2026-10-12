from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_repayment import TransferRepayment, TransferRepaymentDict


class TransferRepaymentListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/repayment/list``"""

    repayments: list[TransferRepayment]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferRepaymentListResponseDict(TypedDict):
    repayments: list[TransferRepaymentDict]
    request_id: str
