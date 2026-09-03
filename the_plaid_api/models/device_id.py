from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceId(SdkBaseModel):
    """Device ID associated with the device used during the previous Link session"""

    type_: Optional[int] = Field(default=UNSET, alias="type")
    id: Optional[str] = UNSET
    """Identifier for the device"""


class DeviceIdDict(TypedDict):
    type_: NotRequired[int]
    id: NotRequired[str]
