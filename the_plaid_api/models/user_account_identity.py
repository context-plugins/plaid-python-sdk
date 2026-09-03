from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .user_account_identity_address import UserAccountIdentityAddress, UserAccountIdentityAddressDict
from .user_account_identity_name import UserAccountIdentityName, UserAccountIdentityNameDict


class UserAccountIdentity(SdkBaseModel):
    """The identity data permissioned by the end user during the authorization flow."""

    name: OptionalNullable[UserAccountIdentityName] = UNSET
    """The user's first name and last name."""

    address: OptionalNullable[UserAccountIdentityAddress] = UNSET
    """The user's address."""

    phone_number: Optional[str] = UNSET
    """The user's phone number in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format"""

    email: OptionalNullable[str] = UNSET
    """The user's email address.

    Note: email is currently not returned."""

    date_of_birth: OptionalNullable[str] = UNSET
    """The user's date of birth."""

    ssn: OptionalNullable[str] = UNSET
    """The user's Social Security number."""

    ssn_last_4: OptionalNullable[str] = UNSET
    """The last 4 digits of the user's Social Security number."""


class UserAccountIdentityDict(TypedDict):
    name: NotRequired[UserAccountIdentityName | UserAccountIdentityNameDict | None]
    address: NotRequired[UserAccountIdentityAddress | UserAccountIdentityAddressDict | None]
    phone_number: NotRequired[str]
    email: NotRequired[str | None]
    date_of_birth: NotRequired[str | None]
    ssn: NotRequired[str | None]
    ssn_last_4: NotRequired[str | None]
