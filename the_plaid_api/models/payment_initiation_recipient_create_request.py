from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict
from .recipient_bacsnullable import RecipientBacsnullable, RecipientBacsnullableDict


class PaymentInitiationRecipientCreateRequest(SdkBaseModel):
    """PaymentInitiationRecipientCreateRequest defines the request schema for
    ``/payment_initiation/recipient/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    name: str
    """The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure
    compatibility with all institutions."""

    iban: OptionalNullable[str] = UNSET
    """The International Bank Account Number (IBAN) for the recipient. If Bacs data is not provided, an IBAN is
    required."""

    bacs: OptionalNullable[RecipientBacsnullable] = UNSET
    """An object containing a Bacs account number and sort code. If an IBAN is not provided or if this recipient needs
    to accept domestic GBP-denominated payments, Bacs data is required."""

    address: OptionalNullable[PaymentInitiationAddress] = UNSET
    """The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""


class PaymentInitiationRecipientCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    name: str
    iban: NotRequired[str | None]
    bacs: NotRequired[RecipientBacsnullable | RecipientBacsnullableDict | None]
    address: NotRequired[PaymentInitiationAddress | PaymentInitiationAddressDict | None]
