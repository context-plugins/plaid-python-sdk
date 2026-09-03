from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferDevice(SdkBaseModel):
    """Information about the device being used to initiate the authorization."""

    ip_address: str
    """The IP address of the device being used to initiate the authorization."""

    user_agent: str
    """The user agent of the device being used to initiate the authorization."""


class TransferDeviceDict(TypedDict):
    ip_address: str
    user_agent: str
