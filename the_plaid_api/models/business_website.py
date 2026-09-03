from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BusinessWebsite(SdkBaseModel):
    """Website associated with a business"""

    url: str | None
    """URL of the business website"""


class BusinessWebsiteDict(TypedDict):
    url: str | None
