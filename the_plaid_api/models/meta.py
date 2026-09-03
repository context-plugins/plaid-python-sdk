from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Meta(SdkBaseModel):
    """Allows specifying the metadata of the test account"""

    name: str
    """The account's name"""

    official_name: str
    """The account's official name"""

    limit: float
    """The account's limit"""

    mask: str
    """The account's mask. Should be an empty string or a string of 2-4 alphanumeric characters. This allows you to
    model a mask which does not match the account number (such as with a virtual account number)."""


class MetaDict(TypedDict):
    name: str
    official_name: str
    limit: float
    mask: str
