from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.entity_watchlist_code import EntityWatchlistCodeOrStr
from .enums.program_name_sensitivity import ProgramNameSensitivityOrStr
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail, WatchlistScreeningAuditTrailDict


class WatchlistScreeningEntityProgramGetResponse(SdkBaseModel):
    """A program that configures the active lists, search parameters, and other behavior for initial and ongoing
    screening of entities."""

    id: str
    """ID of the associated entity program."""

    created_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    is_rescanning_enabled: bool
    """Indicator specifying whether the program is enabled and will perform daily rescans."""

    lists_enabled: list[EntityWatchlistCodeOrStr]
    """Watchlists enabled for the associated program"""

    name: str
    """A name for the entity program to define its purpose. For example, "High Risk Organizations" or "Applicants"."""

    name_sensitivity: ProgramNameSensitivityOrStr
    """The valid name matching sensitivity configurations for a screening program. Note that while certain matching
    techniques may be more prevalent on less strict settings, all matching algorithms are enabled for every sensitivity.

    ``coarse`` - See more potential matches. This sensitivity will see more broad phonetic matches across alphabets that
    make missing a potential hit very unlikely. This setting is noisier and will require more manual review.

    ``balanced`` - A good default for most companies. This sensitivity is balanced to show high quality hits with
    reduced noise.

    ``strict`` - Aggressive false positive reduction. This sensitivity will require names to be more similar than
    ``coarse`` and ``balanced`` settings, relying less on phonetics, while still accounting for character
    transpositions, missing tokens, and other common permutations.

    ``exact`` - Matches must be nearly exact. This sensitivity will only show hits with exact or nearly exact name
    matches with only basic correction such as extraneous symbols and capitalization. This setting is generally not
    recommended unless you have a very specific use case."""

    audit_trail: WatchlistScreeningAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it
    occurred."""

    is_archived: bool
    """Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WatchlistScreeningEntityProgramGetResponseDict(TypedDict):
    id: str
    created_at: RFC3339DateTime
    is_rescanning_enabled: bool
    lists_enabled: list[EntityWatchlistCodeOrStr]
    name: str
    name_sensitivity: ProgramNameSensitivityOrStr
    audit_trail: WatchlistScreeningAuditTrail | WatchlistScreeningAuditTrailDict
    is_archived: bool
    request_id: str
