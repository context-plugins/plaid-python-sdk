from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class NewAccountsAvailableWebhook(SdkBaseModel):
    """Fired when Plaid detects a new account. Upon receiving this webhook, you can prompt your users to share new
    accounts with you through `update mode
    <https://plaid.com/docs/link/update-mode/#using-update-mode-to-request-new-accounts>`__ (US/CA only). If the end
    user has opted not to share new accounts with Plaid via their institution's OAuth settings, Plaid will not detect
    new accounts and this webhook will not fire. For end user accounts in the EU and UK, upon receiving this webhook,
    you can prompt your user to re-link their account and then delete the old Item via ``/item/remove``."""

    webhook_type: Optional[str] = UNSET
    """``ITEM``"""

    webhook_code: Optional[str] = UNSET
    """``NEW_ACCOUNTS_AVAILABLE``"""

    item_id: Optional[str] = UNSET
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    environment: Optional[WebhookEnvironmentValuesOrStr] = UNSET
    """The Plaid environment the webhook was sent from"""


class NewAccountsAvailableWebhookDict(TypedDict):
    webhook_type: NotRequired[str]
    webhook_code: NotRequired[str]
    item_id: NotRequired[str]
    user_id: NotRequired[str]
    error: NotRequired[ErrorDict | None]
    environment: NotRequired[WebhookEnvironmentValuesOrStr]
