from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .client_user_identity import ClientUserIdentity, ClientUserIdentityDict
from .consumer_report_user_identity import ConsumerReportUserIdentity, ConsumerReportUserIdentityDict


class UserUpdateRequest(SdkBaseModel):
    """UserUpdateRequest defines the request schema for ``/user/update``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    identity: OptionalNullable[ClientUserIdentity] = UNSET
    """The identity fields associated with a user. For a user to be eligible for a Plaid Check Consumer Report, all
    fields are required except ``id_number``. Providing a partial SSN is strongly recommended, and improves the accuracy
    of matching user records during compliance processes such as file disclosure, dispute, or security freeze requests.
    If creating a report that will be shared with GSEs such as Fannie or Freddie, a full Social Security Number must be
    provided via the ``id_number`` field."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    consumer_report_user_identity: OptionalNullable[ConsumerReportUserIdentity] = UNSET
    """This field is only used by integrations created before December 10, 2025. All other integrations must use the
    ``identity`` object instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__.
    To create a Plaid Check Consumer Report for a user when using a ``user_token``, this field must be present. If this
    field is not provided during user token creation, you can add it to the user later by calling ``/user/update``. Once
    the field has been added to the user, you will be able to call ``/link/token/create`` with a non-empty
    ``consumer_report_permissible_purpose`` (which will automatically create a Plaid Check Consumer Report), or call
    ``/cra/check_report/create`` for that user."""


class UserUpdateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_id: NotRequired[str]
    identity: NotRequired[ClientUserIdentityDict | None]
    user_token: NotRequired[str]
    consumer_report_user_identity: NotRequired[ConsumerReportUserIdentityDict | None]
