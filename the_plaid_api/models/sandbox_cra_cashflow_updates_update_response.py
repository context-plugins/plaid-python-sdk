from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxCraCashflowUpdatesUpdateResponse(SdkBaseModel):
    """SandboxCraCashflowUpdatesUpdateResponse defines the response schema for
    ``/sandbox/cra/cashflow_updates/update``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxCraCashflowUpdatesUpdateResponseDict(TypedDict):
    request_id: str
