from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClientUserIdentityName(SdkBaseModel):
    """User name information."""

    given_name: str
    """User's given name."""

    family_name: str
    """User's family name."""


class ClientUserIdentityNameDict(TypedDict):
    given_name: str
    family_name: str
