from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EntityWatchlistScreeningSearchTerms(SdkBaseModel):
    """Search terms associated with an entity used for searching against watchlists"""

    entity_watchlist_program_id: str
    """ID of the associated entity program."""

    legal_name: str
    """The name of the organization being screened. Must have at least one alphabetical character, have a maximum length
    of 100 characters, and not include leading or trailing spaces."""

    document_number: str | None
    """The numeric or alphanumeric identifier associated with this document. Must be between 4 and 32 characters long,
    and cannot have leading or trailing spaces."""

    email_address: EmailStr | None
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""

    country: str | None
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""

    phone_number: str | None
    """A phone number in E.164 format."""

    url: str | None
    """An 'http' or 'https' URL (must begin with either of those)."""

    version: int
    """The current version of the search terms. Starts at ``1`` and increments with each edit to ``search_terms``."""


class EntityWatchlistScreeningSearchTermsDict(TypedDict):
    entity_watchlist_program_id: str
    legal_name: str
    document_number: str | None
    email_address: EmailStr | None
    country: str | None
    phone_number: str | None
    url: str | None
    version: int
