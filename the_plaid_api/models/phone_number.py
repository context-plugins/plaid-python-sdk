from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type import TypeOrStr


class PhoneNumber(SdkBaseModel):
    """A phone number"""

    data: str
    """The phone number."""

    primary: bool
    """When ``true``, identifies the phone number as the primary number on an account."""

    type_: TypeOrStr = Field(alias="type")
    """The type of phone number."""


class PhoneNumberDict(TypedDict):
    data: str
    primary: bool
    type_: TypeOrStr
