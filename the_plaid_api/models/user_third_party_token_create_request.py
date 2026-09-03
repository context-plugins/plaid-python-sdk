from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class UserThirdPartyTokenCreateRequest(SdkBaseModel):
    """UserThirdPartyTokenCreateRequest defines the request schema for ``/user/third_party_token/create``"""

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

    third_party_client_id: str
    """The Plaid API ``client_id`` of the third-party client the token will be shared with. The token will only be valid
    for the specified client."""

    expiration_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The expiration date and time for the third-party user token in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format (``YYYY-MM-DDThh:mm:ssZ``). The expiration is restricted to a maximum of 24 hours from the token's creation
    time. If not provided, the token will automatically expire after 24 hours."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""


class UserThirdPartyTokenCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_token: NotRequired[str]
    third_party_client_id: str
    expiration_time: NotRequired[RFC3339DateTime | None]
    user_id: NotRequired[str]
