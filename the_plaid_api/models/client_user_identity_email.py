from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClientUserIdentityEmail(SdkBaseModel):
    """User email information."""

    data: str
    """User's email."""

    primary: bool
    """Indicates whether this is the primary email for the User."""


class ClientUserIdentityEmailDict(TypedDict):
    data: str
    primary: bool
