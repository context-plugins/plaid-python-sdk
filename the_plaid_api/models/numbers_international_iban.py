from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersInternationalIban(SdkBaseModel):
    """Account numbers using the International Bank Account Number and BIC/SWIFT code format."""

    iban: str
    """International Bank Account Number (IBAN)."""

    bic: str
    """The Business Identifier Code, also known as SWIFT code, for this bank account."""


class NumbersInternationalIbanDict(TypedDict):
    iban: str
    bic: str
