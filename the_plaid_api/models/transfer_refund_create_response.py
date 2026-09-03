from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_refund import TransferRefund, TransferRefundDict


class TransferRefundCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/refund/create``"""

    refund: TransferRefund
    """Represents a refund within the Transfers API."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferRefundCreateResponseDict(TypedDict):
    refund: TransferRefund | TransferRefundDict
    request_id: str
