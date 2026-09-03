from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaymentInitiationAddress(SdkBaseModel):
    """The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""

    street: list[str]
    """An array of length 1-2 representing the street address where the recipient is located. Maximum of 70
    characters."""

    city: str
    """The city where the recipient is located. Maximum of 35 characters."""

    postal_code: str
    """The postal code where the recipient is located. Maximum of 16 characters."""

    country: str
    """The ISO 3166-1 alpha-2 country code where the recipient is located."""


class PaymentInitiationAddressDict(TypedDict):
    street: list[str]
    city: str
    postal_code: str
    country: str
