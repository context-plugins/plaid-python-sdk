from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TransferWireDetails(SdkBaseModel):
    """Information specific to wire transfers."""

    message_to_beneficiary: OptionalNullable[str] = UNSET
    """Additional information from the wire originator to the beneficiary. Max 140 characters."""

    wire_return_fee: OptionalNullable[str] = UNSET
    """The fee amount deducted from the original transfer during a wire return, if applicable."""


class TransferWireDetailsDict(TypedDict):
    message_to_beneficiary: NotRequired[str | None]
    wire_return_fee: NotRequired[str | None]
