from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class ProcessorTokenWebhookUpdate(SdkBaseModel):
    """This webhook is only sent to `Plaid processor partners <https://plaid.com/docs/auth/partnerships/>`__.

    Fired when a processor updates the webhook URL for a processor token via ``/processor/token/webhook/update``."""

    webhook_type: str
    """``PROCESSOR_TOKEN``"""

    webhook_code: str
    """``WEBHOOK_UPDATE_ACKNOWLEDGED``"""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    account_id: str
    """The ID of the account."""

    new_webhook_url: str
    """The new webhook URL."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ProcessorTokenWebhookUpdateDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[Error | ErrorDict | None]
    account_id: str
    new_webhook_url: str
    environment: WebhookEnvironmentValuesOrStr
