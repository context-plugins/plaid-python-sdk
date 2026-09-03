from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class EmployerVerification(SdkBaseModel):
    """An object containing employer data."""

    name: OptionalNullable[str] = UNSET
    """Name of employer."""


class EmployerVerificationDict(TypedDict):
    name: NotRequired[str | None]
