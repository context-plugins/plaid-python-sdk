from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CashflowReportPaymentMeta(SdkBaseModel):
    """Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all
    fields will be ``null``."""

    reference_number: str | None
    """The transaction reference number supplied by the financial institution."""

    ppd_id: str | None
    """The ACH PPD ID for the payer."""

    payee: str | None
    """For transfers, the party that is receiving the transaction."""

    by_order_of: str | None
    """The party initiating a wire transfer. Will be ``null`` if the transaction is not a wire transfer."""

    payer: str | None
    """For transfers, the party that is paying the transaction."""

    payment_method: str | None
    """The type of transfer, e.g. 'ACH'"""

    payment_processor: str | None
    """The name of the payment processor"""

    reason: str | None
    """The payer-supplied description of the transfer."""


class CashflowReportPaymentMetaDict(TypedDict):
    reference_number: str | None
    ppd_id: str | None
    payee: str | None
    by_order_of: str | None
    payer: str | None
    payment_method: str | None
    payment_processor: str | None
    reason: str | None
