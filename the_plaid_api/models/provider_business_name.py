from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProviderBusinessName(SdkBaseModel):
    """Name associated with a business"""

    is_primary: bool
    """Indicates whether this is the primary name for the business."""

    name: str | None
    """The name of the business. Must have at least one character and a maximum length of 500 characters."""


class ProviderBusinessNameDict(TypedDict):
    is_primary: bool
    name: str | None
