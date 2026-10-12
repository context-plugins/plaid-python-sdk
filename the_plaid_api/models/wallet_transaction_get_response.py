from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.type5 import Type5OrStr
from .enums.wallet_payment_scheme import WalletPaymentSchemeOrStr
from .enums.wallet_transaction_failure_reason import WalletTransactionFailureReasonOrStr
from .enums.wallet_transaction_payee_verification_status import WalletTransactionPayeeVerificationStatusOrStr
from .enums.wallet_transaction_status import WalletTransactionStatusOrStr
from .error import Error, ErrorDict
from .wallet_transaction_amount import WalletTransactionAmount, WalletTransactionAmountDict
from .wallet_transaction_counterparty import WalletTransactionCounterparty, WalletTransactionCounterpartyDict
from .wallet_transaction_relation import WalletTransactionRelation, WalletTransactionRelationDict


class WalletTransactionGetResponse(SdkBaseModel):
    """WalletTransactionGetResponse defines the response schema for ``/wallet/transaction/get``"""

    transaction_id: str
    """A unique ID identifying the transaction"""

    wallet_id: str
    """The ID of the e-wallet that this transaction is associated with."""

    reference: str
    """A reference for the transaction"""

    type_: Type5OrStr = Field(alias="type")
    """The type of the transaction. The supported transaction types that are returned are: ``BANK_TRANSFER:`` a
    transaction which credits an e-wallet through an external bank transfer.

    ``PAYOUT:`` a transaction which debits an e-wallet by disbursing funds to a counterparty.

    ``PIS_PAY_IN:`` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more
    information see the `Payment Initiation endpoints <https://plaid.com/docs/api/products/payment-initiation/>`__.

    ``REFUND:`` a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid's
    `PIS APIs <https://plaid.com/docs/api/products/payment-initiation/>`__.

    ``FUNDS_SWEEP``: an automated transaction which debits funds from an e-wallet to a designated client-owned account.

    ``RETURN``: an automated transaction where a debit transaction was reversed and money moved back to originating
    account.

    ``RECALL``: a transaction where the sending bank has requested the return of funds due to a fraud claim, technical
    error, or other issue associated with the payment.

    ``ACCOUNT_FUNDING``: an incoming transfer from an allowlisted account. Not automatically refunded.

    ``AUTO_REFUND``: an outgoing refund automatically initiated by Plaid in response to an unexpected
    ``BANK_TRANSFER``."""

    scheme: OptionalNullable[WalletPaymentSchemeOrStr] = UNSET
    """The payment scheme used to execute this transaction. This is present only for transaction types ``PAYOUT`` and
    ``REFUND``.

    ``FASTER_PAYMENTS``: The standard payment scheme within the UK.

    ``SEPA_CREDIT_TRANSFER``: The standard payment to a beneficiary within the SEPA area.

    ``SEPA_CREDIT_TRANSFER_INSTANT``: Instant payment to a beneficiary within the SEPA area."""

    amount: WalletTransactionAmount
    """The amount and currency of a transaction"""

    counterparty: WalletTransactionCounterparty
    """An object representing the e-wallet transaction's counterparty"""

    status: WalletTransactionStatusOrStr
    """The status of the transaction.

    ``AUTHORISING``: The transaction is being processed for validation and compliance.

    ``INITIATED``: The transaction has been initiated and is currently being processed.

    ``EXECUTED``: The transaction has been successfully executed and is considered complete. This is only applicable for
    debit transactions.

    ``SETTLED``: The transaction has settled and funds are available for use. This is only applicable for credit
    transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is
    used.

    ``FAILED``: The transaction failed to process successfully. This is a terminal status.

    ``BLOCKED``: The transaction has been blocked for violating compliance rules. This is a terminal status."""

    created_at: RFC3339DateTime
    """Timestamp when the transaction was created, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    last_status_update: RFC3339DateTime
    """The date and time of the last time the ``status`` was updated, in ISO 8601 format"""

    payee_verification_status: OptionalNullable[WalletTransactionPayeeVerificationStatusOrStr] = UNSET
    """Result of payee verification check for EUR payouts. Payee verification checks whether the payee name provided
    matches the account holder name at the destination institution.

    ``FULL_MATCH``: The payee name fully matches the account holder.

    ``PARTIAL_MATCH``: The payee name partially matches the account holder.

    ``NO_MATCH``: The payee name does not match the account holder.

    ``ERROR``: An error occurred during payee verification.

    ``CHECK_NOT_POSSIBLE``: Payee verification could not be performed.

    This field is only populated for applicable EUR payout transactions and will be ``null`` for other transaction
    types."""

    payment_id: OptionalNullable[str] = UNSET
    """The payment id that this transaction is associated with, if any. This is present only for transaction types
    ``PIS_PAY_IN`` and ``REFUND``."""

    failure_reason: OptionalNullable[WalletTransactionFailureReasonOrStr] = UNSET
    """The error code of a failed transaction. Error codes include: ``EXTERNAL_SYSTEM``: The transaction was declined by
    an external system. ``EXPIRED``: The transaction request has expired. ``CANCELLED``: The transaction request was
    rescinded. ``INVALID``: The transaction did not meet certain criteria, such as an inactive account or no valid
    counterparty, etc. ``ACCOUNT_INVALID``: The transaction could not be processed because the wallet account is invalid
    or inactive. ``AUTHENTICATION_FAILED``: The transaction could not be processed because authentication with the
    wallet provider failed. ``UNKNOWN``: The transaction was unsuccessful, but the exact cause is unknown."""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    related_transactions: Optional[list[WalletTransactionRelation]] = UNSET
    """A list of wallet transactions that this transaction is associated with, if any."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WalletTransactionGetResponseDict(TypedDict):
    transaction_id: str
    wallet_id: str
    reference: str
    type_: Type5OrStr
    scheme: NotRequired[WalletPaymentSchemeOrStr | None]
    amount: WalletTransactionAmountDict
    counterparty: WalletTransactionCounterpartyDict
    status: WalletTransactionStatusOrStr
    created_at: RFC3339DateTime
    last_status_update: RFC3339DateTime
    payee_verification_status: NotRequired[WalletTransactionPayeeVerificationStatusOrStr | None]
    payment_id: NotRequired[str | None]
    failure_reason: NotRequired[WalletTransactionFailureReasonOrStr | None]
    error: NotRequired[ErrorDict | None]
    related_transactions: NotRequired[list[WalletTransactionRelationDict]]
    request_id: str
