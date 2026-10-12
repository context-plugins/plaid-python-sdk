from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .identity_verification_create_request_user import (
    IdentityVerificationCreateRequestUser,
    IdentityVerificationCreateRequestUserDict,
)


class IdentityVerificationCreateRequest(SdkBaseModel):
    """Request schema for ``/identity_verification/create``"""

    client_user_id: Optional[str] = UNSET
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    user_id: Optional[str] = UNSET
    """Unique user identifier, created by calling ``/user/create``. Either a ``user_id`` or the ``client_user_id`` must
    be provided. The ``user_id`` may only be used instead of the ``client_user_id`` if you were not a pre-existing user
    of ``/user/create`` as of December 10, 2025, or if you have since `migrated to the new User APIs
    <https://plaid.com/docs/api/users/migrate-to-new-user-apis>`__; for more details, see `New User APIs
    <https://plaid.com/docs/api/users/user-apis>`__. If both this field and a ``client_user_id`` are present in a
    request, the ``user_id`` must have been created from the provided ``client_user_id``."""

    is_shareable: bool
    """A flag specifying whether you would like Plaid to expose a shareable URL for the verification being created."""

    template_id: str
    """ID of the associated Identity Verification template. Like all Plaid identifiers, this is case-sensitive."""

    gave_consent: bool = False
    """A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be
    shared with Plaid for verification purposes.

    If ``gave_consent`` is set to ``true``, the ``accept_tos`` step will be marked as ``skipped`` and the end user's
    session will start at the next step requirement."""

    user: OptionalNullable[IdentityVerificationCreateRequestUser] = UNSET
    """User information collected outside of Link, most likely via your own onboarding process.

    Each of the following identity fields are optional:

    ``email_address``

    ``phone_number``

    ``date_of_birth``

    ``name``

    ``address``

    ``id_number``

    Specifically, these fields are optional in that they can either be fully provided (satisfying every required field
    in their subschema) or omitted from the request entirely by not providing the key or value. Providing these fields
    via the API will result in Link skipping the data collection process for the associated user. All verification steps
    enabled in the associated Identity Verification Template will still be run. Verification steps will either be run
    immediately, or once the user completes the ``accept_tos`` step, depending on the value provided to the
    ``gave_consent`` field. If you are not using the shareable URL feature, you can optionally provide these fields via
    ``/link/token/create`` instead; both ``/identity_verification/create`` and ``/link/token/create`` are valid ways to
    provide this information. Note that if you provide a non-``null`` user data object via
    ``/identity_verification/create``, any user data fields entered via ``/link/token/create`` for the same
    ``client_user_id`` will be ignored when prefilling Link.

    The ``ip_address`` field is optional. Provide the end user's IP address to enable IP-based risk checks for
    backend-only integrations that do not use the Link SDK; when the Link SDK is used, the IP address is collected
    automatically. Unlike the identity fields above, ``ip_address`` cannot be provided via ``/link/token/create``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    is_idempotent: OptionalNullable[bool] = UNSET
    """An optional flag specifying how you would like Plaid to handle attempts to create an Identity Verification when
    an Identity Verification already exists for the provided ``client_user_id`` and/or ``user_id``, and ``template_id``.
    If idempotency is enabled, Plaid will return the existing Identity Verification. If idempotency is disabled, Plaid
    will reject the request with a ``400 Bad Request`` status code if an Identity Verification already exists for the
    supplied ``client_user_id`` and/or ``user_id``, and ``template_id``."""


class IdentityVerificationCreateRequestDict(TypedDict):
    client_user_id: NotRequired[str]
    user_id: NotRequired[str]
    is_shareable: bool
    template_id: str
    gave_consent: bool
    user: NotRequired[IdentityVerificationCreateRequestUserDict | None]
    client_id: NotRequired[str]
    secret: NotRequired[str]
    is_idempotent: NotRequired[bool | None]
