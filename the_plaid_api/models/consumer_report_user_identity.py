from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .address_data import AddressData, AddressDataDict


class ConsumerReportUserIdentity(SdkBaseModel):
    """This field is only used by integrations created before December 10, 2025. All other integrations must use the
    ``identity`` object instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__.
    To create a Plaid Check Consumer Report for a user when using a ``user_token``, this field must be present. If this
    field is not provided during user token creation, you can add it to the user later by calling ``/user/update``. Once
    the field has been added to the user, you will be able to call ``/link/token/create`` with a non-empty
    ``consumer_report_permissible_purpose`` (which will automatically create a Plaid Check Consumer Report), or call
    ``/cra/check_report/create`` for that user."""

    first_name: str
    """The user's first name"""

    last_name: str
    """The user's last name"""

    phone_numbers: list[str]
    """The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14157452130". Phone numbers
    provided in other formats will be parsed on a best-effort basis. Phone number input is validated against valid
    number ranges; number strings that do not match a real-world phone numbering scheme may cause the request to fail,
    even in the Sandbox test environment."""

    emails: list[str]
    """The user's emails"""

    ssn_full: OptionalNullable[str] = UNSET
    """The user's full Social Security number. This field should only be provided by lenders intending to share the
    resulting consumer report with a Government-Sponsored Enterprise (GSE), such as Fannie Mae or Freddie Mac.

    Format: "ddd-dd-dddd"
    """

    ssn_last_4: OptionalNullable[str] = UNSET
    """The last 4 digits of the user's Social Security number."""

    date_of_birth: Date | None
    """To be provided in the format "yyyy-mm-dd". This field is required for all Plaid Check customers."""

    primary_address: AddressData
    """Data about the components comprising an address."""


class ConsumerReportUserIdentityDict(TypedDict):
    first_name: str
    last_name: str
    phone_numbers: list[str]
    emails: list[str]
    ssn_full: NotRequired[str | None]
    ssn_last_4: NotRequired[str | None]
    date_of_birth: Date | None
    primary_address: AddressData | AddressDataDict
