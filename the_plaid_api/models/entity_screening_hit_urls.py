from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EntityScreeningHitUrls(SdkBaseModel):
    """URLs associated with the entity screening hit"""

    url: str
    """An 'http' or 'https' URL (must begin with either of those)."""


class EntityScreeningHitUrlsDict(TypedDict):
    url: str
