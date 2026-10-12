from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .business_email_address import BusinessEmailAddress, BusinessEmailAddressDict
from .business_phone_number import BusinessPhoneNumber, BusinessPhoneNumberDict
from .business_website import BusinessWebsite, BusinessWebsiteDict
from .enums.business_entity_type import BusinessEntityTypeOrStr
from .provider_business_address import ProviderBusinessAddress, ProviderBusinessAddressDict
from .provider_business_name import ProviderBusinessName, ProviderBusinessNameDict


class BusinessKybmatchDetails(SdkBaseModel):
    """Detailed information about the business from data provider results"""

    names: list[ProviderBusinessName]
    """Names associated with the business."""

    entity_type: BusinessEntityTypeOrStr | None
    """The legal structure or type of business entity"""

    addresses: list[ProviderBusinessAddress]
    """Addresses associated with the business"""

    phone_numbers: list[BusinessPhoneNumber]
    """Phone numbers associated with the business"""

    email_addresses: list[BusinessEmailAddress]
    """Email addresses associated with the business"""

    websites: list[BusinessWebsite]
    """Websites associated with the business"""

    formation_date: Date | None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""


class BusinessKybmatchDetailsDict(TypedDict):
    names: list[ProviderBusinessNameDict]
    entity_type: BusinessEntityTypeOrStr | None
    addresses: list[ProviderBusinessAddressDict]
    phone_numbers: list[BusinessPhoneNumberDict]
    email_addresses: list[BusinessEmailAddressDict]
    websites: list[BusinessWebsiteDict]
    formation_date: Date | None
