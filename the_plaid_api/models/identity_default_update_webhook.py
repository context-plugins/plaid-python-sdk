from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class IdentityDefaultUpdateWebhook(SdkBaseModel):
    """Fired when a change to identity data has been detected on an Item. Items are checked for identity updates every
    30-90 days. We recommend that upon receiving this webhook you make another call to ``/identity/get`` to fetch the
    user's latest identity data."""

    webhook_type: str
    """``IDENTITY``"""

    webhook_code: str
    """``DEFAULT_UPDATE``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    account_ids_with_updated_identity: dict[str, Any]
    """An object with keys of ``account_id``'s that are mapped to their respective identity attributes that changed.

    Example: ``{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["PHONES"] }``"""

    error: Error | None
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class IdentityDefaultUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    account_ids_with_updated_identity: dict[str, Any]
    error: Error | ErrorDict | None
    environment: WebhookEnvironmentValuesOrStr
