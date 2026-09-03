from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .address1 import Address1, Address1Dict
from .id_number import IdNumber, IdNumberDict
from .name2 import Name2, Name2Dict


class LinkTokenCreateRequestUser(SdkBaseModel):
    """An object specifying information about the end user who will be linking their account. **Required** if
    ``user_id`` isn't included."""

    client_user_id: str
    """A unique ID representing the end user. Typically this will be a user ID number from your application. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``. It
    is currently used as a means of searching logs for the given user in the Plaid Dashboard."""

    legal_name: Optional[str] = UNSET
    """The user's full legal name, used for `micro-deposit based verification flows
    <https://plaid.com/docs/auth/coverage/>`__. For a small number of customers on legacy flows, providing this field is
    required to enable micro-deposit-based flows. For all other customers, this field is optional. Providing the user's
    name in this field when using micro-deposit-based verification will streamline the end user experience, as the user
    will not be prompted to enter their name during the Link flow; Plaid will use the provided legal name instead."""

    name: OptionalNullable[Name2] = UNSET
    phone_number: Optional[str] = UNSET
    """The user's phone number in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format. If supplied, will be used when
    applicable to prefill phone number fields in Link for the `returning user flow
    <https://plaid.com/docs/link/returning-user>`__ and the `Identity Verification flow
    <https://plaid.com/docs/identity-verification>`__. Phone number input is validated against valid number ranges;
    number strings that do not match a real-world phone numbering scheme may cause the request to fail, even in the
    Sandbox test environment."""

    phone_number_verified_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time the phone number was verified in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (``YYYY-MM-DDThh:mm:ssZ``). This was previously an optional field used in the `returning user experience
    <https://plaid.com/docs/link/returning-user>`__. This field is no longer required to enable the returning user
    experience.

     Only pass a verification time for a phone number that you have verified. If you have performed verification but
        don't have the time, you may supply a signal value of the start of the UNIX epoch.

     Example: ``2020-01-01T00:00:00Z``"""

    email_address: Optional[str] = UNSET
    """The user's email address. Can be used to prefill Link fields when used with `Identity Verification
    <https://plaid.com/docs/identity-verification>`__."""

    email_address_verified_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time the email address was verified in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (``YYYY-MM-DDThh:mm:ssZ``). This was previously an optional field used in the `returning user experience
    <https://plaid.com/docs/link/returning-user>`__. This field is no longer required to enable the returning user
    experience.

     Only pass a verification time for an email address that you have verified. If you have performed verification but
        don't have the time, you may supply a signal value of the start of the UNIX epoch.

     Example: ``2020-01-01T00:00:00Z``"""

    ssn: Optional[str] = UNSET
    """Deprecated and not currently used, use the ``id_number`` field instead."""

    date_of_birth: OptionalNullable[Date] = UNSET
    """To be provided in the format "yyyy-mm-dd". Can be used to prefill Link fields when used with Identity
    Verification."""

    address: OptionalNullable[Address1] = UNSET
    id_number: OptionalNullable[IdNumber] = UNSET


class LinkTokenCreateRequestUserDict(TypedDict):
    client_user_id: str
    legal_name: NotRequired[str]
    name: NotRequired[Name2 | Name2Dict | None]
    phone_number: NotRequired[str]
    phone_number_verified_time: NotRequired[RFC3339DateTime | None]
    email_address: NotRequired[str]
    email_address_verified_time: NotRequired[RFC3339DateTime | None]
    ssn: NotRequired[str]
    date_of_birth: NotRequired[Date | None]
    address: NotRequired[Address1 | Address1Dict | None]
    id_number: NotRequired[IdNumber | IdNumberDict | None]
