from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxUserResetLoginResponse(SdkBaseModel):
    """SandboxUserResetLoginResponse defines the response schema for ``/sandbox/user/reset_login``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxUserResetLoginResponseDict(TypedDict):
    request_id: str
