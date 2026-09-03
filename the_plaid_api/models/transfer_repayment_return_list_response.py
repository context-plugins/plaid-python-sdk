from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_repayment_return import TransferRepaymentReturn, TransferRepaymentReturnDict


class TransferRepaymentReturnListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/repayment/return/list``"""

    repayment_returns: list[TransferRepaymentReturn]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferRepaymentReturnListResponseDict(TypedDict):
    repayment_returns: list[TransferRepaymentReturn | TransferRepaymentReturnDict]
    request_id: str
