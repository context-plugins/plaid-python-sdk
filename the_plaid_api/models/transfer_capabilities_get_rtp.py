from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferCapabilitiesGetRtp(SdkBaseModel):
    """Contains the supported service types in RTP"""

    credit: Optional[bool] = UNSET
    """When ``true``, the linked Item's institution supports RTP credit transfer."""


class TransferCapabilitiesGetRtpDict(TypedDict):
    credit: NotRequired[bool]
