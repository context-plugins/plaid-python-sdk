from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .entity_screening_hit_analysis import EntityScreeningHitAnalysis, EntityScreeningHitAnalysisDict
from .entity_screening_hit_data import EntityScreeningHitData, EntityScreeningHitDataDict
from .enums.entity_watchlist_code import EntityWatchlistCodeOrStr
from .enums.watchlist_screening_hit_status import WatchlistScreeningHitStatusOrStr


class EntityWatchlistScreeningHit(SdkBaseModel):
    """Data from a government watchlist that has been attached to the screening."""

    id: str
    """ID of the associated entity screening hit."""

    review_status: WatchlistScreeningHitStatusOrStr
    """The current state of review. All watchlist screening hits begin in a ``pending_review`` state but can be changed
    by creating a review. When a hit is in the ``pending_review`` state, it will always show the latest version of the
    watchlist data Plaid has available and be compared against the latest customer information saved in the watchlist
    screening. Once a hit has been marked as ``confirmed`` or ``dismissed`` it will no longer be updated so that the
    state is as it was when the review was first conducted."""

    first_active: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    inactive_since: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    historical_since: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    list_code: EntityWatchlistCodeOrStr
    """Shorthand identifier for a specific screening list for entities.
     ``AU_CON``: Australia Department of Foreign Affairs and Trade Consolidated List
     ``CA_CON``: Government of Canada Consolidated List of Sanctions
     ``EU_CON``: European External Action Service Consolidated List
     ``IZ_SOE``: State Owned Enterprise List
     ``IZ_UNC``: United Nations Consolidated Sanctions
     ``IZ_WBK``: World Bank Listing of Ineligible Firms and Individuals
     ``US_CAP``: US OFAC Correspondent Account or Payable-Through Account Sanctions
     ``US_FSE``: US OFAC Foreign Sanctions Evaders
     ``US_MBS``: US Non-SDN Menu-Based Sanctions
     ``US_SDN``: US OFAC Specially Designated Nationals List
     ``US_SSI``: US OFAC Sectoral Sanctions Identifications
     ``US_CMC``: US OFAC Non-SDN Chinese Military-Industrial Complex List
     ``US_UVL``: Bureau of Industry and Security Unverified List
     ``US_SAM``: US System for Award Management Exclusion List
     ``US_TEL``: US Terrorist Exclusion List
     ``UK_HMC``: Foreign, Commonwealth & Development Office UK Sanctions List"""

    plaid_uid: str
    """A universal identifier for a watchlist individual that is stable across searches and updates."""

    source_uid: str | None
    """The identifier provided by the source sanction or watchlist. When one is not provided by the source, this is
    ``null``."""

    sub_programs: list[str]
    """Sub-program designations that may be attached to the watchlist entry by the issuing authority. For OFAC SDN
    entries these are the program codes published in the SDN list (for example ``SDGT`` for Specially Designated Global
    Terrorists, ``SDNTK`` for Specially Designated Narcotics Trafficking Kingpins, ``IRAN``, ``RUSSIA-EO14024``). New
    codes are added by sanctioning authorities without prior notice, so callers should treat unknown values as opaque
    strings rather than enum members."""

    analysis: Optional[EntityScreeningHitAnalysis] = UNSET
    """Analysis information describing why a screening hit matched the provided entity information"""

    data: Optional[EntityScreeningHitData] = UNSET
    """Information associated with the entity watchlist hit"""


class EntityWatchlistScreeningHitDict(TypedDict):
    id: str
    review_status: WatchlistScreeningHitStatusOrStr
    first_active: RFC3339DateTime
    inactive_since: RFC3339DateTime | None
    historical_since: RFC3339DateTime | None
    list_code: EntityWatchlistCodeOrStr
    plaid_uid: str
    source_uid: str | None
    sub_programs: list[str]
    analysis: NotRequired[EntityScreeningHitAnalysisDict]
    data: NotRequired[EntityScreeningHitDataDict]
