from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CreditSessionError(SdkBaseModel):
    """The details of a Link error."""

    error_type: Optional[str] = UNSET
    """A broad categorization of the error."""

    error_code: Optional[str] = UNSET
    """The particular error code."""

    error_message: Optional[str] = UNSET
    """A developer-friendly representation of the error code."""

    display_message: OptionalNullable[str] = UNSET
    """A user-friendly representation of the error code. ``null`` if the error is not related to user action."""


class CreditSessionErrorDict(TypedDict):
    error_type: NotRequired[str]
    error_code: NotRequired[str]
    error_message: NotRequired[str]
    display_message: NotRequired[str | None]
