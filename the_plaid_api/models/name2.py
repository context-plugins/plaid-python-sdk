from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Name2(SdkBaseModel):
    given_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""

    family_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""


class Name2Dict(TypedDict):
    given_name: str
    family_name: str
