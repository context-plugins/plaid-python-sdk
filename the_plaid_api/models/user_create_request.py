from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .client_user_identity import ClientUserIdentity, ClientUserIdentityDict
from .consumer_report_user_identity import ConsumerReportUserIdentity, ConsumerReportUserIdentityDict


class UserCreateRequest(SdkBaseModel):
    """UserCreateRequest defines the request schema for ``/user/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_user_id: str
    """A unique ID representing the end user. Maximum of 128 characters. Typically this will be a user ID number from
    your application. Personally identifiable information, such as an email address or phone number, should not be used
    in the ``client_user_id``."""

    identity: OptionalNullable[ClientUserIdentity] = UNSET
    """The identity fields associated with a user. For a user to be eligible for a Plaid Check Consumer Report, all
    fields are required except ``id_number``. Providing a partial SSN is strongly recommended, and improves the accuracy
    of matching user records during compliance processes such as file disclosure, dispute, or security freeze requests.
    If creating a report that will be shared with GSEs such as Fannie or Freddie, a full Social Security Number must be
    provided via the ``id_number`` field."""

    end_customer: Optional[str] = UNSET
    """A unique ID representing a CRA reseller's end customer. Maximum of 128 characters."""

    consumer_report_user_identity: OptionalNullable[ConsumerReportUserIdentity] = UNSET
    """This field is only used by integrations created before December 10, 2025. All other integrations must use the
    ``identity`` object instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__.
    To create a Plaid Check Consumer Report for a user when using a ``user_token``, this field must be present. If this
    field is not provided during user token creation, you can add it to the user later by calling ``/user/update``. Once
    the field has been added to the user, you will be able to call ``/link/token/create`` with a non-empty
    ``consumer_report_permissible_purpose`` (which will automatically create a Plaid Check Consumer Report), or call
    ``/cra/check_report/create`` for that user."""

    with_upgraded_user: Optional[bool] = UNSET
    """If your integration with the User API predates December 10, 2025, set this field to ``true`` to opt into the `New
    User APIs <https://plaid.com/docs/api/users/user-apis/>`__. When enabled, you can use the ``identity`` field instead
    of ``consumer_report_user_identity``."""


class UserCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    client_user_id: str
    identity: NotRequired[ClientUserIdentityDict | None]
    end_customer: NotRequired[str]
    consumer_report_user_identity: NotRequired[ConsumerReportUserIdentityDict | None]
    with_upgraded_user: NotRequired[bool]
