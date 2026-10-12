from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payment_initiation_standing_order_metadata import (
    PaymentInitiationStandingOrderMetadata,
    PaymentInitiationStandingOrderMetadataDict,
)


class PaymentInitiationMetadata(SdkBaseModel):
    """Metadata that captures what specific payment configurations an institution supports when making Payment
    Initiation requests."""

    supports_international_payments: bool
    """Indicates whether the institution supports payments from a different country."""

    supports_sepa_instant: bool
    """Indicates whether the institution supports SEPA Instant payments."""

    maximum_payment_amount: dict[str, str]
    """A mapping of currency to maximum payment amount (denominated in the smallest unit of currency) supported by the
    institution.

    Example: ``{"GBP": "10000"}``"""

    supports_refund_details: bool
    """Indicates whether the institution supports returning refund details when initiating a payment."""

    standing_order_metadata: PaymentInitiationStandingOrderMetadata | None
    """Metadata specifically related to valid Payment Initiation standing order configurations for the institution."""

    supports_payment_consents: bool
    """Indicates whether the institution supports payment consents."""


class PaymentInitiationMetadataDict(TypedDict):
    supports_international_payments: bool
    supports_sepa_instant: bool
    maximum_payment_amount: dict[str, str]
    supports_refund_details: bool
    standing_order_metadata: PaymentInitiationStandingOrderMetadataDict | None
    supports_payment_consents: bool
