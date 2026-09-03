from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .originator import Originator, OriginatorDict


class TransferOriginatorListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/originator/list``"""

    originators: list[Originator]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferOriginatorListResponseDict(TypedDict):
    originators: list[Originator | OriginatorDict]
    request_id: str
