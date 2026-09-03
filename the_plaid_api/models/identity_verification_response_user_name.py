from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IdentityVerificationResponseUserName(SdkBaseModel):
    """The full name provided by the user. If the user has not submitted their name, this field will be null. Otherwise,
    both fields are guaranteed to be filled."""

    given_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""

    family_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""


class IdentityVerificationResponseUserNameDict(TypedDict):
    given_name: str
    family_name: str
