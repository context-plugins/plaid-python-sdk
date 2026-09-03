from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReceiverDetails(SdkBaseModel):
    """Additional details for receiver events. Currently always ``null``."""

    available_balance: str | None
    """The available balance associated with the receiver event."""


class ReceiverDetailsDict(TypedDict):
    available_balance: str | None
