from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class IdentityVerificationListRequest(SdkBaseModel):
    """Request input for listing Identity Verifications"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    template_id: str
    """ID of the associated Identity Verification template. Like all Plaid identifiers, this is case-sensitive."""

    client_user_id: Optional[str] = UNSET
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    user_id: OptionalNullable[str] = UNSET
    """A unique user identifier, created by calling ``/user/create``. Either a ``user_id`` or the ``client_user_id``
    must be provided. The ``user_id`` may only be used instead of the ``client_user_id`` if you were not a pre-existing
    user of ``/user/create`` as of December 10, 2025, or if you have since `migrated to the new User APIs
    <https://plaid.com/docs/api/users/migrate-to-new-user-apis>`__; for more details, see `New User APIs
    <https://plaid.com/docs/api/users/user-apis>`__. If both this field and the ``client_user_id`` are present in the
    request, the ``user_id`` must have been created from the provided ``client_user_id``."""

    cursor: OptionalNullable[str] = UNSET
    """An identifier that determines which page of results you receive."""


class IdentityVerificationListRequestDict(TypedDict):
    secret: NotRequired[str]
    client_id: NotRequired[str]
    template_id: str
    client_user_id: NotRequired[str]
    user_id: NotRequired[str | None]
    cursor: NotRequired[str | None]
