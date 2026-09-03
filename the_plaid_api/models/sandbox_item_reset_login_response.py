from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxItemResetLoginResponse(SdkBaseModel):
    """SandboxItemResetLoginResponse defines the response schema for ``/sandbox/item/reset_login``"""

    reset_login: bool
    """``true`` if the call succeeded"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxItemResetLoginResponseDict(TypedDict):
    reset_login: bool
    request_id: str
