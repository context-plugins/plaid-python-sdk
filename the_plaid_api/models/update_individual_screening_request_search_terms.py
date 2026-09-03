from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class UpdateIndividualScreeningRequestSearchTerms(SdkBaseModel):
    """Search terms for editing an individual watchlist screening"""

    watchlist_program_id: Optional[str] = UNSET
    """ID of the associated program."""

    legal_name: Optional[str] = UNSET
    """The legal name of the individual being screened. Must have at least one alphabetical character, have a maximum
    length of 100 characters, and not include leading or trailing spaces."""

    date_of_birth: Optional[Date] = UNSET
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    document_number: Optional[str] = UNSET
    """The numeric or alphanumeric identifier associated with this document. Must be between 4 and 32 characters long,
    and cannot have leading or trailing spaces."""

    country: Optional[str] = UNSET
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""


class UpdateIndividualScreeningRequestSearchTermsDict(TypedDict):
    watchlist_program_id: NotRequired[str]
    legal_name: NotRequired[str]
    date_of_birth: NotRequired[Date]
    document_number: NotRequired[str]
    country: NotRequired[str]
