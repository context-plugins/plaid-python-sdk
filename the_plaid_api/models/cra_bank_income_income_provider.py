from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraBankIncomeIncomeProvider(SdkBaseModel):
    """The object containing data about the income provider."""

    name: str
    """The name of the income provider."""

    is_normalized: bool
    """Indicates whether the income provider name is normalized by comparing it against a canonical set of known
    providers."""


class CraBankIncomeIncomeProviderDict(TypedDict):
    name: str
    is_normalized: bool
