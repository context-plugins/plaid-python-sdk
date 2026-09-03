from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class HistoricalUpdateWebhook(SdkBaseModel):
    """Fired when an Item's historical transaction pull is completed and Plaid has prepared as much historical
    transaction data as possible for the Item. Once this webhook has been fired, transaction data beyond the most recent
    30 days can be fetched for the Item. This webhook will also be fired if account selections for the Item are updated,
    with ``new_transactions`` set to the number of net new transactions pulled after the account selection update.

    This webhook is intended for use with ``/transactions/get``; if you are using the newer ``/transactions/sync``
    endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for
    and respond to the ``SYNC_UPDATES_AVAILABLE`` webhook instead."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``HISTORICAL_UPDATE``"""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    new_transactions: float
    """The number of new transactions available"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class HistoricalUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[Error | ErrorDict | None]
    new_transactions: float
    item_id: str
    environment: WebhookEnvironmentValuesOrStr
