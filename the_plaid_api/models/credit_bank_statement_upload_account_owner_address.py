from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditBankStatementUploadAccountOwnerAddress(SdkBaseModel):
    """Address on the uploaded bank statement"""

    city: str | None
    """The full city name."""

    country: str | None
    """The ISO 3166-1 alpha-2 country code."""

    postal_code: str | None
    """The postal code of the address."""

    region: str | None
    """The region or state. Example: ``"NC"``"""

    street: str | None
    """The full street address."""


class CreditBankStatementUploadAccountOwnerAddressDict(TypedDict):
    city: str | None
    country: str | None
    postal_code: str | None
    region: str | None
    street: str | None
