from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class W2Box12(SdkBaseModel):
    """Data on the W2 Box 12"""

    code: OptionalNullable[str] = UNSET
    """W2 Box 12 code."""

    amount: OptionalNullable[str] = UNSET
    """W2 Box 12 amount."""


class W2Box12Dict(TypedDict):
    code: NotRequired[str | None]
    amount: NotRequired[str | None]
