from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_business_address import ResponseBusinessAddress, ResponseBusinessAddressDict


class BusinessSearchTerms(SdkBaseModel):
    """The business information that was used to perform the verification search"""

    name: str | None
    """The name of the business. Must have at least one character and a maximum length of 500 characters."""

    alternative_names: list[str]
    """Alternative business names that were submitted as search inputs."""

    address: ResponseBusinessAddress
    """Physical address of a business. Used for response schemas."""

    website: str | None
    """An 'http' or 'https' URL (must begin with either of those)."""

    phone_number: str | None
    """A phone number in E.164 format."""

    email_address: EmailStr | None
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""


class BusinessSearchTermsDict(TypedDict):
    name: str | None
    alternative_names: list[str]
    address: ResponseBusinessAddressDict
    website: str | None
    phone_number: str | None
    email_address: EmailStr | None
