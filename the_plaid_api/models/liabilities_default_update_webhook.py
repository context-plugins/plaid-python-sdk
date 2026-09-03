from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class LiabilitiesDefaultUpdateWebhook(SdkBaseModel):
    """The webhook of type ``LIABILITIES`` and code ``DEFAULT_UPDATE`` will be fired when new or updated liabilities
    have been detected on a liabilities item."""

    webhook_type: str
    """``LIABILITIES``"""

    webhook_code: str
    """``DEFAULT_UPDATE``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    error: Error | None
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    account_ids_with_new_liabilities: list[str]
    """An array of ``account_id``'s for accounts that contain new liabilities.'"""

    account_ids_with_updated_liabilities: dict[str, Any]
    """An object with keys of ``account_id``'s that are mapped to their respective liabilities fields that changed.

    Example: ``{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["past_amount_due"] }``"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class LiabilitiesDefaultUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    error: Error | ErrorDict | None
    account_ids_with_new_liabilities: list[str]
    account_ids_with_updated_liabilities: dict[str, Any]
    environment: WebhookEnvironmentValuesOrStr
