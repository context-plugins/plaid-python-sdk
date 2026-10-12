from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.payment_initiation_payment_status import PaymentInitiationPaymentStatusOrStr
from .enums.payment_scheme import PaymentSchemeOrStr
from .error import Error, ErrorDict
from .external_payment_refund_details import ExternalPaymentRefundDetails, ExternalPaymentRefundDetailsDict
from .external_payment_schedule_get import ExternalPaymentScheduleGet, ExternalPaymentScheduleGetDict
from .payment_amount import PaymentAmount, PaymentAmountDict
from .payment_amount_refunded import PaymentAmountRefunded, PaymentAmountRefundedDict
from .sender_bacsnullable import SenderBacsnullable, SenderBacsnullableDict


class PaymentInitiationPayment(SdkBaseModel):
    """PaymentInitiationPayment defines a payment initiation payment"""

    payment_id: str
    """The ID of the payment. Like all Plaid identifiers, the ``payment_id`` is case sensitive."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    status: PaymentInitiationPaymentStatusOrStr
    """The status of the payment.

    Core lifecycle statuses:

    **``PAYMENT_STATUS_INPUT_NEEDED``**: Transitional. The payment is awaiting user input to continue processing. It may
    re-enter this state if additional input is required.

    **``PAYMENT_STATUS_AUTHORISING``:** Transitional. The payment is being authorised by the financial institution. It
    will automatically move on once authorisation completes.

    **``PAYMENT_STATUS_INITIATED``:** The payment has been authorised and accepted by the financial institution. In many
    EU markets, ``PAYMENT_STATUS_EXECUTED`` is not supported, and a payment will remain in ``PAYMENT_STATUS_INITIATED``
    until the funds settle, making this a terminal success state in those cases. A payment in
    ``PAYMENT_STATUS_INITIATED`` should be treated as a successfully submitted payment; do not gate downstream
    processing on reaching ``PAYMENT_STATUS_EXECUTED``. For a full explanation of payment statuses and how to handle
    each, see the `Payment Status guide <https://plaid.com/docs/payment-initiation/payment-status/>`__.

    **``PAYMENT_STATUS_EXECUTED``: Terminal.** The funds have left the payer's account and the payment is en route to
    settlement. Note that this status does not confirm that funds have arrived in the recipient's account; do not use it
    as proof of fund receipt. Support is more common in the UK than in the EU; where unsupported, a successful payment
    remains in ``PAYMENT_STATUS_INITIATED`` before settling. When using Plaid Virtual Accounts,
    ``PAYMENT_STATUS_EXECUTED`` is not terminal -- the payment will continue to ``PAYMENT_STATUS_SETTLED`` once funds
    are available.

    **``PAYMENT_STATUS_SETTLED``: Terminal.** The funds are available in the recipient's account. Only available to
    customers using `Plaid Virtual Accounts <https://plaid.com/docs/payment-initiation/virtual-accounts/>`__.

    Failure statuses:

    **``PAYMENT_STATUS_INSUFFICIENT_FUNDS``: Terminal.** The payment failed due to insufficient funds. No further
    retries will succeed until the payer's balance is replenished.

    **``PAYMENT_STATUS_FAILED``: Terminal (retryable).** The payment could not be initiated due to a system error or
    outage. Retry once the root cause is resolved.

    **``PAYMENT_STATUS_BLOCKED``: Terminal (retryable).** The payment was blocked by Plaid (e.g., flagged as risky).
    Resolve any compliance or risk issues and retry.

    **``PAYMENT_STATUS_REJECTED``: Terminal.** The payment was rejected by the financial institution. No automatic retry
    is possible.

    **``PAYMENT_STATUS_CANCELLED``: Terminal.** The end user cancelled the payment during authorisation.

    Standing-order statuses:

    **``PAYMENT_STATUS_ESTABLISHED``: Terminal.** A recurring/standing order has been successfully created.

    Deprecated (to be removed in a future release):

    ``PAYMENT_STATUS_UNKNOWN``: The payment status is unknown.

    ``PAYMENT_STATUS_PROCESSING``: The payment is currently being processed.

    ``PAYMENT_STATUS_COMPLETED``: Indicates that the standing order has been successfully established."""

    recipient_id: str
    """The ID of the recipient"""

    reference: str
    """A reference for the payment."""

    adjusted_reference: OptionalNullable[str] = UNSET
    """The value of the reference sent to the bank after adjustment to pass bank validation rules."""

    last_status_update: RFC3339DateTime
    """The date and time of the last time the ``status`` was updated, in ISO 8601 format"""

    schedule: OptionalNullable[ExternalPaymentScheduleGet] = UNSET
    """The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up
    as a standing order. If no schedule is specified, the payment will be executed only once."""

    refund_details: OptionalNullable[ExternalPaymentRefundDetails] = UNSET
    """Details about external payment refund"""

    bacs: SenderBacsnullable | None
    """An object containing a Bacs account number and sort code. If an IBAN is not provided or if this recipient needs
    to accept domestic GBP-denominated payments, Bacs data is required."""

    iban: str | None
    """The International Bank Account Number (IBAN) for the sender, if specified in the
    ``/payment_initiation/payment/create`` call."""

    refund_ids: OptionalNullable[list[str]] = UNSET
    """Refund IDs associated with the payment."""

    amount_refunded: OptionalNullable[PaymentAmountRefunded] = UNSET
    """The amount and currency of a payment"""

    wallet_id: OptionalNullable[str] = UNSET
    """The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an
    intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""

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

    adjusted_scheme: OptionalNullable[PaymentSchemeOrStr] = UNSET
    """Payment scheme. If not specified - the default in the region will be used (e.g. ``SEPA_CREDIT_TRANSFER`` for EU).
    In responses, if the scheme is not explicitly specified in the request, this value will be ``null``. Using
    unsupported values will result in a failed payment.

    ``LOCAL_DEFAULT``: The default payment scheme for the selected market and currency will be used.

    ``LOCAL_INSTANT``: The instant payment scheme for the selected market and currency will be used (if applicable).
    Fees may be applied by the institution.

    ``SEPA_CREDIT_TRANSFER``: The standard payment to a beneficiary within the SEPA area.

    ``SEPA_CREDIT_TRANSFER_INSTANT``: Instant payment within the SEPA area. May involve additional fees and may not be
    available at some banks."""

    consent_id: OptionalNullable[str] = UNSET
    """The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the
    payment consent."""

    transaction_id: OptionalNullable[str] = UNSET
    """The transaction ID that this payment is associated with, if any. This is present only when a payment was
    initiated using virtual accounts."""

    end_to_end_id: OptionalNullable[str] = UNSET
    """A unique identifier assigned by Plaid to each payment for tracking and reconciliation purposes.

    Note: Not all banks handle ``end_to_end_id`` consistently. To ensure accurate matching, clients should convert both
    the incoming ``end_to_end_id`` and the one provided by Plaid to the same case (either lower or upper) before
    comparison. For virtual account payments, Plaid manages this field automatically."""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""


class PaymentInitiationPaymentDict(TypedDict):
    payment_id: str
    amount: PaymentAmountDict
    status: PaymentInitiationPaymentStatusOrStr
    recipient_id: str
    reference: str
    adjusted_reference: NotRequired[str | None]
    last_status_update: RFC3339DateTime
    schedule: NotRequired[ExternalPaymentScheduleGetDict | None]
    refund_details: NotRequired[ExternalPaymentRefundDetailsDict | None]
    bacs: SenderBacsnullableDict | None
    iban: str | None
    refund_ids: NotRequired[list[str] | None]
    amount_refunded: NotRequired[PaymentAmountRefundedDict | None]
    wallet_id: NotRequired[str | None]
    scheme: NotRequired[PaymentSchemeOrStr | None]
    adjusted_scheme: NotRequired[PaymentSchemeOrStr | None]
    consent_id: NotRequired[str | None]
    transaction_id: NotRequired[str | None]
    end_to_end_id: NotRequired[str | None]
    error: NotRequired[ErrorDict | None]
