from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .session_token_create_request_user import SessionTokenCreateRequestUser, SessionTokenCreateRequestUserDict


class SessionTokenCreateRequest(SdkBaseModel):
    """SessionTokenCreateRequest defines the request schema for ``/session/token/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    template_id: str
    """The id of a template defined in Plaid Dashboard"""

    user: Optional[SessionTokenCreateRequestUser] = UNSET
    """Details about the end user. Required if a root-level ``user_id`` is not provided."""

    redirect_uri: Optional[str] = UNSET
    """A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support
    OAuth authentication flows when launching Link in the browser or another app. The ``redirect_uri`` should not
    contain any query parameters. When used in Production, must be an https URI. Note that any redirect URI must also be
    added to the Allowed redirect URIs list in the `developer dashboard <https://dashboard.plaid.com/team/api>`__. If
    initializing on Android, ``android_package_name`` must be specified instead and ``redirect_uri`` should be left
    blank."""

    android_package_name: Optional[str] = UNSET
    """The name of your app's Android package. Required if using the session token to initialize Layer on Android. Any
    package name specified here must also be added to the Allowed Android package names setting on the `developer
    dashboard <https://dashboard.plaid.com/team/api>`__. When creating a session token for initializing Layer on other
    platforms, ``android_package_name`` must be left blank and ``redirect_uri`` should be used instead."""

    webhook: Optional[str] = UNSET
    """The destination URL to which any webhooks should be sent. If you use the same webhook listener for all Sandbox or
    all Production activity, set this value in the Layer template editor in the Dashboard instead. Only provide a value
    in this field if you need to use multiple webhook URLs per environment (an uncommon use case). If provided, a value
    in this field will take priority over webhook values set in the Layer template editor."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""


class SessionTokenCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    template_id: str
    user: NotRequired[SessionTokenCreateRequestUser | SessionTokenCreateRequestUserDict]
    redirect_uri: NotRequired[str]
    android_package_name: NotRequired[str]
    webhook: NotRequired[str]
    user_id: NotRequired[str]
