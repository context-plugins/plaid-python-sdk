from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .request_business_address import RequestBusinessAddress, RequestBusinessAddressDict


class BusinessVerificationCreateRequestBusiness(SdkBaseModel):
    """Business information provided in the verification request"""

    name: Optional[str] = UNSET
    """The name of the business. Must have at least one character and a maximum length of 500 characters."""

    alternative_name: OptionalNullable[str] = UNSET
    """The name of the business. Must have at least one character and a maximum length of 500 characters."""

    address: Optional[RequestBusinessAddress] = UNSET
    """Physical address of a business. Used for input requests."""

    website: Optional[str] = UNSET
    """An 'http' or 'https' URL (must begin with either of those)."""

    phone_number: Optional[str] = UNSET
    """A phone number in E.164 format."""

    email_address: Optional[EmailStr] = UNSET
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""


class BusinessVerificationCreateRequestBusinessDict(TypedDict):
    name: NotRequired[str]
    alternative_name: NotRequired[str | None]
    address: NotRequired[RequestBusinessAddress | RequestBusinessAddressDict]
    website: NotRequired[str]
    phone_number: NotRequired[str]
    email_address: NotRequired[EmailStr]
