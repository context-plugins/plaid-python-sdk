from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class ProcessorTransactionsRemovedWebhook(SdkBaseModel):
    """This webhook is only sent to `Plaid processor partners <https://plaid.com/docs/auth/partnerships/>`__.

    Fired when transaction(s) for an Item are deleted. The deleted transaction IDs are included in the webhook payload.
    Plaid will typically check for deleted transaction data several times a day.

    This webhook is intended for use with ``/processor/transactions/get``; if you are using the newer
    ``/processor/transactions/sync`` endpoint, this webhook will still be fired to maintain backwards compatibility, but
    it is recommended to listen for and respond to the ``SYNC_UPDATES_AVAILABLE`` webhook instead."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``TRANSACTIONS_REMOVED``"""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    removed_transactions: list[str]
    """An array of ``transaction_ids`` corresponding to the removed transactions"""

    account_id: str
    """The ID of the account."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ProcessorTransactionsRemovedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[Error | ErrorDict | None]
    removed_transactions: list[str]
    account_id: str
    environment: WebhookEnvironmentValuesOrStr
