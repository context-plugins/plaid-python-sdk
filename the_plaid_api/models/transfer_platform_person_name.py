from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferPlatformPersonName(SdkBaseModel):
    """The person's legal name"""

    given_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""

    family_name: str
    """A string with at least one non-whitespace character, with a max length of 100 characters."""


class TransferPlatformPersonNameDict(TypedDict):
    given_name: str
    family_name: str
