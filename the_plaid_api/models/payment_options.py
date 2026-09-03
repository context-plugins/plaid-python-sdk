from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.payment_scheme import PaymentSchemeOrStr
from .payment_initiation_optional_restriction_bacs import (
    PaymentInitiationOptionalRestrictionBacs,
    PaymentInitiationOptionalRestrictionBacsDict,
)


class PaymentOptions(SdkBaseModel):
    """Additional payment options"""

    request_refund_details: OptionalNullable[bool] = UNSET
    """When ``true``, Plaid will attempt to request refund details from the payee's financial institution. Support
    varies between financial institutions and will not always be available. If refund details could be retrieved, they
    will be available in the ``/payment_initiation/payment/get`` response."""

    iban: OptionalNullable[str] = UNSET
    """The International Bank Account Number (IBAN) for the payer's account. Where possible, the end user will be able
    to send payments only from the specified bank account if provided."""

    bacs: OptionalNullable[PaymentInitiationOptionalRestrictionBacs] = UNSET
    """An optional object used to restrict the accounts used for payments. If provided, the end user will be able to
    send payments only from the specified bank account."""

    scheme: OptionalNullable[PaymentSchemeOrStr] = UNSET
    """Payment scheme. If not specified - the default in the region will be used (e.g. ``SEPA_CREDIT_TRANSFER`` for EU).
    In responses, if the scheme is not explicitly specified in the request, this value will be ``null``. Using
    unsupported values will result in a failed payment.

    ``LOCAL_DEFAULT``: The default payment scheme for the selected market and currency will be used.

    ``LOCAL_INSTANT``: The instant payment scheme for the selected market and currency will be used (if applicable).
    Fees may be applied by the institution.

    ``SEPA_CREDIT_TRANSFER``: The standard payment to a beneficiary within the SEPA area.

    ``SEPA_CREDIT_TRANSFER_INSTANT``: Instant payment within the SEPA area. May involve additional fees and may not be
    available at some banks."""


class PaymentOptionsDict(TypedDict):
    request_refund_details: NotRequired[bool | None]
    iban: NotRequired[str | None]
    bacs: NotRequired[PaymentInitiationOptionalRestrictionBacs | PaymentInitiationOptionalRestrictionBacsDict | None]
    scheme: NotRequired[PaymentSchemeOrStr | None]
