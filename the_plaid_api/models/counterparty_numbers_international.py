from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CounterpartyNumbersInternational(SdkBaseModel):
    """Account numbers using the International Bank Account Number and BIC/SWIFT code format."""

    iban: OptionalNullable[str] = UNSET
    """International Bank Account Number (IBAN)."""

    bic: OptionalNullable[str] = UNSET
    """Business Identifier Code (BIC) for this counterparty."""


class CounterpartyNumbersInternationalDict(TypedDict):
    iban: NotRequired[str | None]
    bic: NotRequired[str | None]
