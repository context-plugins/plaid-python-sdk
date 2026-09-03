from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class WatchlistScreeningSearchTerms(SdkBaseModel):
    """Search terms for creating an individual watchlist screening"""

    watchlist_program_id: str
    """ID of the associated program."""

    legal_name: str
    """The legal name of the individual being screened. Must have at least one alphabetical character, have a maximum
    length of 100 characters, and not include leading or trailing spaces."""

    date_of_birth: Date | None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    document_number: str | None
    """The numeric or alphanumeric identifier associated with this document. Must be between 4 and 32 characters long,
    and cannot have leading or trailing spaces."""

    country: str | None
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""

    version: int
    """The current version of the search terms. Starts at ``1`` and increments with each edit to ``search_terms``."""


class WatchlistScreeningSearchTermsDict(TypedDict):
    watchlist_program_id: str
    legal_name: str
    date_of_birth: Date | None
    document_number: str | None
    country: str | None
    version: int
