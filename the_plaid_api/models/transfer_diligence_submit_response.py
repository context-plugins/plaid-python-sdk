from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferDiligenceSubmitResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/diligence/submit``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferDiligenceSubmitResponseDict(TypedDict):
    request_id: str
