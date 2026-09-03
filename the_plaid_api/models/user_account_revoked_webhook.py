from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class UserAccountRevokedWebhook(SdkBaseModel):
    """The ``USER_ACCOUNT_REVOKED`` webhook is fired when an end user has revoked access to their account on the Data
    Provider's portal. This webhook is currently sent only for PNC Items, but may be sent in the future for other
    financial institutions that allow account-level permissions revocation through their portals. Upon receiving this
    webhook, it is recommended to delete any Plaid-derived data you have stored that is associated with the revoked
    account.

    If you are using Auth and receive this webhook, this webhook indicates that the TAN associated with the revoked
    account is no longer valid and cannot be used to create new transfers. You should not create new ACH transfers for
    the account that was revoked until access has been re-granted.

    You can request the user to re-grant access to their account by sending them through `update mode
    <https://plaid.com/docs/link/update-mode>`__. Alternatively, they may re-grant access directly through the Data
    Provider's portal.

    After the user has re-granted access, Auth customers should call the auth endpoint again to obtain the new TAN."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``USER_ACCOUNT_REVOKED``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    account_id: str
    """The external account ID of the affected account"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class UserAccountRevokedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    account_id: str
    environment: WebhookEnvironmentValuesOrStr
