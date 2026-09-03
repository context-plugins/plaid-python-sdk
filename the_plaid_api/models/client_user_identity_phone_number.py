from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClientUserIdentityPhoneNumber(SdkBaseModel):
    """User phone number information."""

    data: str
    """User's phone number."""

    primary: bool
    """Indicates whether this is the primary phone number for the User."""


class ClientUserIdentityPhoneNumberDict(TypedDict):
    data: str
    primary: bool
