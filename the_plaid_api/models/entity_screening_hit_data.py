from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .entity_screening_hit_documents_items import EntityScreeningHitDocumentsItems, EntityScreeningHitDocumentsItemsDict
from .entity_screening_hit_emails_items import EntityScreeningHitEmailsItems, EntityScreeningHitEmailsItemsDict
from .entity_screening_hit_names_items import EntityScreeningHitNamesItems, EntityScreeningHitNamesItemsDict
from .entity_screening_hit_urls_items import EntityScreeningHitUrlsItems, EntityScreeningHitUrlsItemsDict
from .entity_screening_hits_phone_number_items import (
    EntityScreeningHitsPhoneNumberItems,
    EntityScreeningHitsPhoneNumberItemsDict,
)
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems, GenericScreeningHitLocationItemsDict


class EntityScreeningHitData(SdkBaseModel):
    """Information associated with the entity watchlist hit"""

    documents: Optional[list[EntityScreeningHitDocumentsItems]] = UNSET
    """Documents associated with the watchlist hit"""

    email_addresses: Optional[list[EntityScreeningHitEmailsItems]] = UNSET
    """Email addresses associated with the watchlist hit"""

    locations: Optional[list[GenericScreeningHitLocationItems]] = UNSET
    """Locations associated with the watchlist hit"""

    names: Optional[list[EntityScreeningHitNamesItems]] = UNSET
    """Names associated with the watchlist hit"""

    phone_numbers: Optional[list[EntityScreeningHitsPhoneNumberItems]] = UNSET
    """Phone numbers associated with the watchlist hit"""

    urls: Optional[list[EntityScreeningHitUrlsItems]] = UNSET
    """URLs associated with the watchlist hit"""


class EntityScreeningHitDataDict(TypedDict):
    documents: NotRequired[list[EntityScreeningHitDocumentsItems | EntityScreeningHitDocumentsItemsDict]]
    email_addresses: NotRequired[list[EntityScreeningHitEmailsItems | EntityScreeningHitEmailsItemsDict]]
    locations: NotRequired[list[GenericScreeningHitLocationItems | GenericScreeningHitLocationItemsDict]]
    names: NotRequired[list[EntityScreeningHitNamesItems | EntityScreeningHitNamesItemsDict]]
    phone_numbers: NotRequired[list[EntityScreeningHitsPhoneNumberItems | EntityScreeningHitsPhoneNumberItemsDict]]
    urls: NotRequired[list[EntityScreeningHitUrlsItems | EntityScreeningHitUrlsItemsDict]]
