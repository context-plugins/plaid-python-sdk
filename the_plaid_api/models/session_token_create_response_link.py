from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class SessionTokenCreateResponseLink(SdkBaseModel):
    """Response data for ``/session/token/create`` intended for use with the Link SDK."""

    link_token: str
    """A Link token, which can be supplied to Link in order to initialize it and receive a ``public_token``."""

    expiration: RFC3339DateTime
    """The expiration date for the ``link_token``, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format. A
    ``link_token`` created to generate a ``public_token`` that will be exchanged for a new ``access_token`` expires
    after 4 hours. A ``link_token`` created for an existing Item (such as when updating an existing ``access_token`` by
    launching Link in update mode) expires after 30 minutes."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""


class SessionTokenCreateResponseLinkDict(TypedDict):
    link_token: str
    expiration: RFC3339DateTime
    user_id: NotRequired[str]
