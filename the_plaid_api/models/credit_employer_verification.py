from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditEmployerVerification(SdkBaseModel):
    """An object containing employer data."""

    name: str | None
    """Name of employer."""


class CreditEmployerVerificationDict(TypedDict):
    name: str | None
