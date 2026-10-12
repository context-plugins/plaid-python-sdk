from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.wallet_transaction_failure_reason import WalletTransactionFailureReasonOrStr
from .enums.wallet_transaction_status import WalletTransactionStatusOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class WalletTransactionStatusUpdateWebhook(SdkBaseModel):
    """Fired when the status of a wallet transaction has changed."""

    webhook_type: str
    """``WALLET``"""

    webhook_code: str
    """``WALLET_TRANSACTION_STATUS_UPDATE``"""

    transaction_id: str
    """The ``transaction_id`` for the wallet transaction being updated"""

    payment_id: OptionalNullable[str] = UNSET
    """The ``payment_id`` associated with the transaction. This will be present in case of ``REFUND`` and
    ``PIS_PAY_IN``."""

    wallet_id: Optional[str] = UNSET
    """The EMI (E-Money Institution) wallet that this payment is associated with. This wallet is used as an intermediary
    account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""

    new_status: WalletTransactionStatusOrStr
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

    old_status: WalletTransactionStatusOrStr
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

    failure_reason: OptionalNullable[WalletTransactionFailureReasonOrStr] = UNSET
    """The error code of a failed transaction. Error codes include: ``EXTERNAL_SYSTEM``: The transaction was declined by
    an external system. ``EXPIRED``: The transaction request has expired. ``CANCELLED``: The transaction request was
    rescinded. ``INVALID``: The transaction did not meet certain criteria, such as an inactive account or no valid
    counterparty, etc. ``ACCOUNT_INVALID``: The transaction could not be processed because the wallet account is invalid
    or inactive. ``AUTHENTICATION_FAILED``: The transaction could not be processed because authentication with the
    wallet provider failed. ``UNKNOWN``: The transaction was unsuccessful, but the exact cause is unknown."""

    timestamp: RFC3339DateTime
    """The timestamp of the update, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2017-09-14T14:42:19.350Z"``"""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class WalletTransactionStatusUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    transaction_id: str
    payment_id: NotRequired[str | None]
    wallet_id: NotRequired[str]
    new_status: WalletTransactionStatusOrStr
    old_status: WalletTransactionStatusOrStr
    failure_reason: NotRequired[WalletTransactionFailureReasonOrStr | None]
    timestamp: RFC3339DateTime
    error: NotRequired[ErrorDict | None]
    environment: WebhookEnvironmentValuesOrStr
