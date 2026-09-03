from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BusinessEmailAddress(SdkBaseModel):
    """Email address associated with a business"""

    email_address: EmailStr | None
    """Email address of the business"""


class BusinessEmailAddressDict(TypedDict):
    email_address: EmailStr | None
