from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class ItemProductReadyWebhook(SdkBaseModel):
    """Fired once Plaid calculates income from an Item."""

    webhook_type: str
    """``INCOME``"""

    webhook_code: str
    """``PRODUCT_READY``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ItemProductReadyWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: NotRequired[Error | ErrorDict | None]
    environment: WebhookEnvironmentValuesOrStr
