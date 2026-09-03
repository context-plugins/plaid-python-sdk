from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditBankEmployer(SdkBaseModel):
    """Object containing employer data."""

    name: str
    """Name of the employer."""


class CreditBankEmployerDict(TypedDict):
    name: str
