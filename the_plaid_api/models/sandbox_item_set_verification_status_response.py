from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxItemSetVerificationStatusResponse(SdkBaseModel):
    """SandboxItemSetVerificationStatusResponse defines the response schema for
    ``/sandbox/item/set_verification_status``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxItemSetVerificationStatusResponseDict(TypedDict):
    request_id: str
