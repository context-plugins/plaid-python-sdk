from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict
from .recipient_bacsnullable import RecipientBacsnullable, RecipientBacsnullableDict


class PaymentInitiationRecipientGetResponse(SdkBaseModel):
    """PaymentInitiationRecipientGetResponse defines the response schema for ``/payment_initiation/recipient/get``"""

    recipient_id: str
    """The ID of the recipient."""

    name: str
    """The name of the recipient."""

    address: OptionalNullable[PaymentInitiationAddress] = UNSET
    """The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""

    iban: OptionalNullable[str] = UNSET
    """The International Bank Account Number (IBAN) for the recipient."""

    bacs: OptionalNullable[RecipientBacsnullable] = UNSET
    """An object containing a Bacs account number and sort code. If an IBAN is not provided or if this recipient needs
    to accept domestic GBP-denominated payments, Bacs data is required."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationRecipientGetResponseDict(TypedDict):
    recipient_id: str
    name: str
    address: NotRequired[PaymentInitiationAddressDict | None]
    iban: NotRequired[str | None]
    bacs: NotRequired[RecipientBacsnullableDict | None]
    request_id: str
