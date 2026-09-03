from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerEndCustomerTechnicalContact(SdkBaseModel):
    """The technical contact for the end customer. Defaults to partner's technical contact if omitted."""

    given_name: Optional[str] = UNSET
    family_name: Optional[str] = UNSET
    email: Optional[str] = UNSET


class PartnerEndCustomerTechnicalContactDict(TypedDict):
    given_name: NotRequired[str]
    family_name: NotRequired[str]
    email: NotRequired[str]
