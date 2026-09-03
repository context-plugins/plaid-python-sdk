from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SignalEvaluateDevice(SdkBaseModel):
    """Details about the end user's device. These fields are optional, but strongly recommended to increase the accuracy
    of results when using Signal Transaction Scores. When using a Balance-only Ruleset, these fields are ignored if the
    Signal Addendum has been signed; if it has not been signed, using these fields will result in an error."""

    ip_address: OptionalNullable[str] = UNSET
    """The IP address of the device that initiated the transaction"""

    user_agent: OptionalNullable[str] = UNSET
    """The user agent of the device that initiated the transaction (e.g. "Mozilla/5.0")"""


class SignalEvaluateDeviceDict(TypedDict):
    ip_address: NotRequired[str | None]
    user_agent: NotRequired[str | None]
