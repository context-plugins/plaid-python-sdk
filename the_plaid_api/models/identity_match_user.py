from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .address_data_nullable_no_required_fields import (
    AddressDataNullableNoRequiredFields,
    AddressDataNullableNoRequiredFieldsDict,
)


class IdentityMatchUser(SdkBaseModel):
    """The user's legal name, phone number, email address and address used to perform fuzzy match. If Financial Account
    Matching is enabled in the Identity Verification product, leave this field empty to automatically match against PII
    collected from the Identity Verification checks."""

    legal_name: OptionalNullable[str] = UNSET
    """The user's full legal name."""

    phone_number: OptionalNullable[str] = UNSET
    """The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14157452130". Phone numbers
    provided in other formats will be parsed on a best-effort basis. Phone number input is validated against valid
    number ranges; number strings that do not match a real-world phone numbering scheme may cause the request to fail,
    even in the Sandbox test environment."""

    email_address: OptionalNullable[str] = UNSET
    """The user's email address."""

    address: OptionalNullable[AddressDataNullableNoRequiredFields] = UNSET
    """Data about the components comprising an address."""


class IdentityMatchUserDict(TypedDict):
    legal_name: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    email_address: NotRequired[str | None]
    address: NotRequired[AddressDataNullableNoRequiredFieldsDict | None]
