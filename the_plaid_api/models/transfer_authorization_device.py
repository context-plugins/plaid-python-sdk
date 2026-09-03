from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferAuthorizationDevice(SdkBaseModel):
    """Information about the device being used to initiate the authorization. These fields are not currently
    incorporated into the risk check."""

    ip_address: Optional[str] = UNSET
    """The IP address of the device being used to initiate the authorization."""

    user_agent: Optional[str] = UNSET
    """The user agent of the device being used to initiate the authorization."""


class TransferAuthorizationDeviceDict(TypedDict):
    ip_address: NotRequired[str]
    user_agent: NotRequired[str]
