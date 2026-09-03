from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkTokenCreateCardSwitch(SdkBaseModel):
    """A map containing data to pass in for the Card Switch flow."""

    card_bin: str
    """The BIN (Bank Identification Number) of the card to switch."""


class LinkTokenCreateCardSwitchDict(TypedDict):
    card_bin: str
