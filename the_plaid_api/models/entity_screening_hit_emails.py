from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EntityScreeningHitEmails(SdkBaseModel):
    """Email address information for the associated entity watchlist hit"""

    email_address: EmailStr
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""


class EntityScreeningHitEmailsDict(TypedDict):
    email_address: EmailStr
