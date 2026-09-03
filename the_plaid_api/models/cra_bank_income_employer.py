from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraBankIncomeEmployer(SdkBaseModel):
    """The object containing employer data."""

    name: str | None
    """The name of the employer."""


class CraBankIncomeEmployerDict(TypedDict):
    name: str | None
