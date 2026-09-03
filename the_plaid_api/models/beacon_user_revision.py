from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BeaconUserRevision(SdkBaseModel):
    """A Beacon User Revision identifies a Beacon User at some point in its revision history."""

    id: str
    """ID of the associated Beacon User."""

    version: int
    """The ``version`` field begins with 1 and increments with each subsequent revision."""


class BeaconUserRevisionDict(TypedDict):
    id: str
    version: int
