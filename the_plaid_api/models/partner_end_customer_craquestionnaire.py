from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_crapurposes import PartnerEndCustomerCrapurposes, PartnerEndCustomerCrapurposesDict


class PartnerEndCustomerCraquestionnaire(SdkBaseModel):
    """The CRA questionnaire for the end customer."""

    purposes: Optional[PartnerEndCustomerCrapurposes] = UNSET
    """A map of permissible purposes to their corresponding use cases."""

    is_third_party_involved: Optional[bool] = UNSET
    """Denotes whether the third party is involved."""

    is_technical_service_provider_involved: Optional[bool] = UNSET
    """Denotes whether the technical service provider is involved."""


class PartnerEndCustomerCraquestionnaireDict(TypedDict):
    purposes: NotRequired[PartnerEndCustomerCrapurposes | PartnerEndCustomerCrapurposesDict]
    is_third_party_involved: NotRequired[bool]
    is_technical_service_provider_involved: NotRequired[bool]
