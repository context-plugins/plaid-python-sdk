from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.party_registry import PartyRegistryOrStr
from .enums.party_type import PartyTypeOrStr


class PartyEntity(SdkBaseModel):
    """FDX Participant - an entity or person that is a part of a FDX API transaction"""

    name: str
    """Human recognizable common name"""

    type_: PartyTypeOrStr = Field(alias="type")
    """Identifies the type of a party"""

    home_uri: Optional[str] = Field(default=UNSET, alias="homeUri")
    """URI for party, where an end user could learn more about the company or application involved in the data sharing
    chain"""

    logo_uri: Optional[str] = Field(default=UNSET, alias="logoUri")
    """URI for a logo asset to be displayed to the end user"""

    registry: Optional[PartyRegistryOrStr] = UNSET
    """The registry containing the party's registration with name and id"""

    registered_entity_name: Optional[str] = Field(default=UNSET, alias="registeredEntityName")
    """Registered name of party"""

    registered_entity_id: Optional[str] = Field(default=UNSET, alias="registeredEntityId")
    """Registered id of party"""


class PartyEntityDict(TypedDict):
    name: str
    type_: PartyTypeOrStr
    home_uri: NotRequired[str]
    logo_uri: NotRequired[str]
    registry: NotRequired[PartyRegistryOrStr]
    registered_entity_name: NotRequired[str]
    registered_entity_id: NotRequired[str]
