from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BusinessPhoneNumber(SdkBaseModel):
    """Phone number associated with a business"""

    number: str | None
    """Phone number in E.164 format"""


class BusinessPhoneNumberDict(TypedDict):
    number: str | None
