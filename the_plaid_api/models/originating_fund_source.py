from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict


class OriginatingFundSource(SdkBaseModel):
    """The original source of the funds. This field is required by local regulation for certain businesses (e.g. money
    remittance) to send payouts to recipients in the EU and UK."""

    full_name: str
    """The full name associated with the source of the funds."""

    address: PaymentInitiationAddress | None
    """The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""

    account_number: str
    """The account number from which the funds are sourced."""

    bic: str
    """The Business Identifier Code, also known as SWIFT code, for this bank account."""


class OriginatingFundSourceDict(TypedDict):
    full_name: str
    address: PaymentInitiationAddressDict | None
    account_number: str
    bic: str
