from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateEntityScreeningRequestSearchTerms(SdkBaseModel):
    """Search terms for editing an entity watchlist screening"""

    entity_watchlist_program_id: str
    """ID of the associated entity program."""

    legal_name: Optional[str] = UNSET
    """The name of the organization being screened. Must have at least one alphabetical character, have a maximum length
    of 100 characters, and not include leading or trailing spaces."""

    document_number: Optional[str] = UNSET
    """The numeric or alphanumeric identifier associated with this document. Must be between 4 and 32 characters long,
    and cannot have leading or trailing spaces."""

    email_address: Optional[EmailStr] = UNSET
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""

    country: Optional[str] = UNSET
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""

    phone_number: Optional[str] = UNSET
    """A phone number in E.164 format."""

    url: Optional[str] = UNSET
    """An 'http' or 'https' URL (must begin with either of those)."""


class UpdateEntityScreeningRequestSearchTermsDict(TypedDict):
    entity_watchlist_program_id: str
    legal_name: NotRequired[str]
    document_number: NotRequired[str]
    email_address: NotRequired[EmailStr]
    country: NotRequired[str]
    phone_number: NotRequired[str]
    url: NotRequired[str]
