from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxTransactionsCreateResponse(SdkBaseModel):
    """SandboxTransactionsCreateResponse defines the response schema for ``/sandbox/transactions/create``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxTransactionsCreateResponseDict(TypedDict):
    request_id: str
