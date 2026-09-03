from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .client_user_identity import ClientUserIdentity, ClientUserIdentityDict


class UserGetResponse(SdkBaseModel):
    """UserGetResponse defines the response schema for ``/user/get``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    user_id: str
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    client_user_id: str | None
    """Client provided user ID."""

    created_at: RFC3339DateTime
    """Timestamp of user creation."""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp of last user update."""

    identity: OptionalNullable[ClientUserIdentity] = UNSET
    """The identity fields associated with a user. For a user to be eligible for a Plaid Check Consumer Report, all
    fields are required except ``id_number``. Providing a partial SSN is strongly recommended, and improves the accuracy
    of matching user records during compliance processes such as file disclosure, dispute, or security freeze requests.
    If creating a report that will be shared with GSEs such as Fannie or Freddie, a full Social Security Number must be
    provided via the ``id_number`` field."""


class UserGetResponseDict(TypedDict):
    request_id: str
    user_id: str
    client_user_id: str | None
    created_at: RFC3339DateTime
    updated_at: NotRequired[RFC3339DateTime]
    identity: NotRequired[ClientUserIdentity | ClientUserIdentityDict | None]
