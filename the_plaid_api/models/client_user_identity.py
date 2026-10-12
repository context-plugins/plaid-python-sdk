from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .client_user_identity_address import ClientUserIdentityAddress, ClientUserIdentityAddressDict
from .client_user_identity_email import ClientUserIdentityEmail, ClientUserIdentityEmailDict
from .client_user_identity_name import ClientUserIdentityName, ClientUserIdentityNameDict
from .client_user_identity_phone_number import ClientUserIdentityPhoneNumber, ClientUserIdentityPhoneNumberDict
from .user_idnumber import UserIdnumber, UserIdnumberDict


class ClientUserIdentity(SdkBaseModel):
    """The identity fields associated with a user. For a user to be eligible for a Plaid Check Consumer Report, all
    fields are required except ``id_number``. Providing a partial SSN is strongly recommended, and improves the accuracy
    of matching user records during compliance processes such as file disclosure, dispute, or security freeze requests.
    If creating a report that will be shared with GSEs such as Fannie or Freddie, a full Social Security Number must be
    provided via the ``id_number`` field."""

    name: OptionalNullable[ClientUserIdentityName] = UNSET
    """User name information."""

    date_of_birth: OptionalNullable[Date] = UNSET
    """The user's date of birth, to be provided in the format "yyyy-mm-dd"."""

    emails: Optional[list[ClientUserIdentityEmail]] = UNSET
    """The user's emails."""

    phone_numbers: Optional[list[ClientUserIdentityPhoneNumber]] = UNSET
    """The user's phone numbers, in E.164 format: +{countrycode}{number}. For example: "+14157452130". Phone numbers
    provided in other formats will be parsed on a best-effort basis. Phone number input is validated against valid
    number ranges; number strings that do not match a real-world phone numbering scheme may cause the request to fail,
    even in the Sandbox test environment."""

    addresses: Optional[list[ClientUserIdentityAddress]] = UNSET
    """The user's addresses."""

    id_numbers: Optional[list[UserIdnumber | None]] = UNSET
    """The user's ID numbers."""


class ClientUserIdentityDict(TypedDict):
    name: NotRequired[ClientUserIdentityNameDict | None]
    date_of_birth: NotRequired[Date | None]
    emails: NotRequired[list[ClientUserIdentityEmailDict]]
    phone_numbers: NotRequired[list[ClientUserIdentityPhoneNumberDict]]
    addresses: NotRequired[list[ClientUserIdentityAddressDict]]
    id_numbers: NotRequired[list[UserIdnumberDict | None]]
