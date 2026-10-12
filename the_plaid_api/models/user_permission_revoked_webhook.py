from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class UserPermissionRevokedWebhook(SdkBaseModel):
    """The ``USER_PERMISSION_REVOKED`` webhook may be fired when an end user has revoked the permission that they
    previously granted to access an Item. If the end user revoked their permissions through Plaid (such as via the Plaid
    Portal or by contacting Plaid support), the webhook will fire. If the end user revoked their permissions directly
    through the institution, this webhook may not always fire, since some institutions' consent portals do not trigger
    this webhook. To attempt to restore the Item, it can be sent through `update mode
    <https://plaid.com/docs/link/update-mode>`__. Depending on the exact process the end user used to revoke
    permissions, it may not be possible to launch update mode for the Item. If you encounter an error when attempting to
    create a Link token for update mode on an Item with revoked permissions, create a fresh Link token for the user.

    Note that when working with tokenized account numbers with Auth or Transfer, the account number provided by Plaid
    will no longer work for creating transfers once user permission has been revoked, except for US Bank Items."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``USER_PERMISSION_REVOKED``"""

    item_id: str
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

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class UserPermissionRevokedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    error: NotRequired[ErrorDict | None]
    environment: WebhookEnvironmentValuesOrStr
