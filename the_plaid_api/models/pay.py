from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Pay(SdkBaseModel):
    """An object representing a monetary amount."""

    amount: OptionalNullable[float] = UNSET
    """A numerical amount of a specific currency."""

    currency: OptionalNullable[str] = UNSET
    """Currency code, e.g. USD"""


class PayDict(TypedDict):
    amount: NotRequired[float | None]
    currency: NotRequired[str | None]
