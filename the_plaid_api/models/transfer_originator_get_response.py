from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .detailed_originator import DetailedOriginator, DetailedOriginatorDict


class TransferOriginatorGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/originator/get``"""

    originator: DetailedOriginator
    """Originator and their status."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferOriginatorGetResponseDict(TypedDict):
    originator: DetailedOriginatorDict
    request_id: str
