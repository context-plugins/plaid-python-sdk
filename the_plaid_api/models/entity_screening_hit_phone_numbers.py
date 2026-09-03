from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.phone_type import PhoneTypeOrStr


class EntityScreeningHitPhoneNumbers(SdkBaseModel):
    """Phone number information associated with the entity screening hit"""

    type_: PhoneTypeOrStr = Field(alias="type")
    """An enum indicating whether a phone number is a phone line or a fax line."""

    phone_number: str
    """A phone number in E.164 format."""


class EntityScreeningHitPhoneNumbersDict(TypedDict):
    type_: PhoneTypeOrStr
    phone_number: str
