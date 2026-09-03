from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NetworkStatusGetUser(SdkBaseModel):
    """An object specifying information about the end user for the network status check."""

    phone_number: str
    """The user's phone number in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format."""


class NetworkStatusGetUserDict(TypedDict):
    phone_number: str
