from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SandboxUserResetLoginRequest(SdkBaseModel):
    """SandboxUserResetLoginRequest defines the request schema for ``/sandbox/user/reset_login``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    item_ids: OptionalNullable[list[str]] = UNSET
    """An array of ``item_id``s associated with the User to be reset. If empty or ``null``, this field will default to
    resetting all Items associated with the User."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""


class SandboxUserResetLoginRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_token: NotRequired[str]
    item_ids: NotRequired[list[str] | None]
    user_id: NotRequired[str]
