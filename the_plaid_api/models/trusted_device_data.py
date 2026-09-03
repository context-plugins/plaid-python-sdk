from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class TrustedDeviceData(SdkBaseModel):
    """Trusted Device data associated with the previous Link session."""

    trust_level: Optional[int] = UNSET
    device_id: Optional[DeviceId] = UNSET
    """Device ID associated with the device used during the previous Link session"""


class TrustedDeviceDataDict(TypedDict):
    trust_level: NotRequired[int]
    device_id: NotRequired[DeviceId | DeviceIdDict]
