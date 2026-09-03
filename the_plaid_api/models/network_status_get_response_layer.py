from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NetworkStatusGetResponseLayer(SdkBaseModel):
    """An object representing Layer-related metadata for the requested user."""

    eligible: bool
    """Indicates if the user is eligible for a Layer session."""


class NetworkStatusGetResponseLayerDict(TypedDict):
    eligible: bool
