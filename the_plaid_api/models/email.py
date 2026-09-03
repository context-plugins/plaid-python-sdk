from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type1 import Type1OrStr


class Email(SdkBaseModel):
    """An object representing an email address"""

    data: str
    """The email address."""

    primary: bool
    """When ``true``, identifies the email address as the primary email on an account."""

    type_: Type1OrStr = Field(alias="type")
    """The type of email account as described by the financial institution."""


class EmailDict(TypedDict):
    data: str
    primary: bool
    type_: Type1OrStr
