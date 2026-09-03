from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IdentityVerificationRequestUserName(SdkBaseModel):
    """You can use this field to pre-populate the user's legal name; if it is provided here, they will not be prompted
    to enter their name in the identity verification attempt."""

    given_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""

    family_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""


class IdentityVerificationRequestUserNameDict(TypedDict):
    given_name: str
    family_name: str
