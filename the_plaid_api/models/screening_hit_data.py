from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems, GenericScreeningHitLocationItemsDict
from .screening_hit_date_of_birth_item import ScreeningHitDateOfBirthItem, ScreeningHitDateOfBirthItemDict
from .screening_hit_documents_items import ScreeningHitDocumentsItems, ScreeningHitDocumentsItemsDict
from .screening_hit_names_items import ScreeningHitNamesItems, ScreeningHitNamesItemsDict


class ScreeningHitData(SdkBaseModel):
    """Information associated with the watchlist hit"""

    dates_of_birth: Optional[list[ScreeningHitDateOfBirthItem]] = UNSET
    """Dates of birth associated with the watchlist hit"""

    documents: Optional[list[ScreeningHitDocumentsItems]] = UNSET
    """Documents associated with the watchlist hit"""

    locations: Optional[list[GenericScreeningHitLocationItems]] = UNSET
    """Locations associated with the watchlist hit"""

    names: Optional[list[ScreeningHitNamesItems]] = UNSET
    """Names associated with the watchlist hit"""


class ScreeningHitDataDict(TypedDict):
    dates_of_birth: NotRequired[list[ScreeningHitDateOfBirthItemDict]]
    documents: NotRequired[list[ScreeningHitDocumentsItemsDict]]
    locations: NotRequired[list[GenericScreeningHitLocationItemsDict]]
    names: NotRequired[list[ScreeningHitNamesItemsDict]]
